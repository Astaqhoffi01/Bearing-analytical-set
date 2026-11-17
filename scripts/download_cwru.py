"""Unduh dataset CWRU terpilih dan kemas sebagai ZIP.
Jalankan: python -m pip install requests beautifulsoup4
          python download_cwru.py
"""
from pathlib import Path
from urllib.parse import urljoin
import csv, re, time, zipfile
import requests
from bs4 import BeautifulSoup

PAGE_FAULT = 'https://engineering.case.edu/bearingdatacenter/12k-drive-end-bearing-fault-data'
PAGE_NORMAL = 'https://engineering.case.edu/bearingdatacenter/normal-baseline-data'
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUT = PROJECT_ROOT / "data" / "raw" / "CWRU_40_files"
OUT.mkdir(parents=True, exist_ok=True)
S = requests.Session()
S.headers.update({'User-Agent':'Mozilla/5.0 CWRU research downloader'})

def links(page):
    r=S.get(page, timeout=45); r.raise_for_status()
    soup=BeautifulSoup(r.text,'html.parser')
    return [(a.get_text(' ',strip=True),urljoin(page,a['href'])) for a in soup.select('a[href]')]

fault_links=links(PAGE_FAULT)
normal_links=links(PAGE_NORMAL)
selected=[]
for kind, pattern in [('Inner Race',r'^IR(007|014|021)_([0-3])$'),('Ball Fault',r'^B(007|014|021)_([0-3])$'),('Outer Race',r'^OR(007|014|021)@6_([0-3])$')]:
    for title,url in fault_links:
        m=re.fullmatch(pattern,title.strip(),re.I)
        if m:
            selected.append(dict(label=title,condition=kind,fault_size_inch=int(m.group(1))/1000,motor_load_hp=int(m.group(2)),url=url))
# Normal baseline names typically include Normal_0 etc, but select only links in the data table matching load names.
for title,url in normal_links:
    name=title.strip()
    m=re.fullmatch(r'(?:Normal[_ -]?)?([0-3])(?:[_ -]?HP)?',name,re.I)
    if m and url.lower().split('?')[0].endswith('.mat'):
        selected.append(dict(label=name,condition='Normal',fault_size_inch='',motor_load_hp=int(m.group(1)),url=url))
# CWRU normal page also uses names like Normal_0. Fail safely if not all normal labels found.
counts={k:sum(x['condition']==k for x in selected) for k in ['Normal','Inner Race','Ball Fault','Outer Race']}
if counts != {'Normal':4,'Inner Race':12,'Ball Fault':12,'Outer Race':12}:
    print('Ditemukan:',counts)
    print('Tautan Normal:',[(t,u) for t,u in normal_links if '.mat' in u.lower()])
    raise RuntimeError('Daftar tidak lengkap: tidak akan membuat ZIP yang diklaim lengkap. Periksa nama tautan pada situs.')

manifest=[]
for i,item in enumerate(selected,1):
    filename=item['url'].split('?')[0].split('/')[-1]
    path=OUT/filename
    if not path.exists() or path.stat().st_size<1000:
        print(f'[{i}/{len(selected)}] Download {item["label"]}: {filename}',flush=True)
        with S.get(item['url'],stream=True,timeout=120) as r:
            r.raise_for_status()
            with path.open('wb') as f:
                for chunk in r.iter_content(1024*1024):
                    if chunk:f.write(chunk)
        time.sleep(0.3)
    with path.open('rb') as f:
        header=f.read(20)
    if not header.startswith(b'MATLAB'):
        raise ValueError(f'{filename} bukan MATLAB v5 yang diharapkan; cek hasil unduhan')
    manifest.append({**item,'filename':filename,'size_bytes':path.stat().st_size})
with (OUT/'metadata.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=['filename','label','condition','fault_size_inch','motor_load_hp','url','size_bytes']);w.writeheader();w.writerows(manifest)
archive=OUT.parent/'CWRU_40_files.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in OUT.iterdir():z.write(p,arcname=p.name)
print(f'BERHASIL: {archive} ({len(manifest)} file MAT + metadata)')
