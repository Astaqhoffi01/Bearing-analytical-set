CWRU DATASET DOWNLOADER

Tujuan: 40 file .mat: 4 Normal, 12 Inner Race, 12 Ball Fault, 12 Outer Race @6:00.
Fault diameters: 0.007, 0.014, 0.021 inch. Loads: 0, 1, 2, 3 HP.

1. Ekstrak paket ini.
2. Buka PowerShell di folder yang berisi download_cwru.py.
3. Jalankan: python -m pip install requests beautifulsoup4
4. Jalankan: python download_cwru.py
5. Setelah berhasil, file CWRU_40_files.zip dibuat otomatis.

Program mengambil tautan resmi dari website CWRU dan memvalidasi jumlah file.
Apabila situs mengubah nama link, program berhenti tanpa membuat ZIP tidak lengkap.
Sumber: https://engineering.case.edu/bearingdatacenter/12k-drive-end-bearing-fault-data
        https://engineering.case.edu/bearingdatacenter/normal-baseline-data
