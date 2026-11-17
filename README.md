Bearing Fault Diagnosis and Motor Load Analysis Using Vibration Signals

**Digital Signal Processing | Data Engineering | Machine Learning | Predictive Maintenance**

## Project Overview

This project investigates vibration-based bearing condition monitoring using the Case Western Reserve University (CWRU) Bearing Data Center dataset.

The research integrates Digital Signal Processing (DSP), Data Engineering (DE), and Data Science Analytics (DSA) to extract meaningful information from vibration signals and develop machine learning models for bearing analysis.

The project addresses three main analytical objectives:

1. **Bearing Condition Classification** — Identifying normal and faulty bearing conditions.
2. **Bearing Defect Size Estimation** — Estimating the severity of bearing defects.
3. **Motor Load Classification** — Identifying motor operating loads using vibration harmonics.

## Dataset

**Source:** [Case Western Reserve University Bearing Data Center](https://engineering.case.edu/bearingdatacenter)

The study uses vibration recordings representing normal bearings and bearings with different fault types, defect sizes, and motor loads.

The preprocessing pipeline includes sampling-rate standardization, data cleaning, metadata management, and signal segmentation.

## Research Workflow

```text
CWRU Bearing Dataset
         |
         v
Data Ingestion & Preprocessing
         |
         v
Digital Signal Processing
(Filtering, FFT, Welch PSD)
         |
         v
Feature Engineering
         |
         v
Machine Learning Models
         |
         +-- Outcome 1: Bearing Condition Classification
         |
         +-- Outcome 2: Defect Size Estimation
         |
         +-- Outcome 3: Motor Load Classification
         |
         v
Model Evaluation & Visualization
```

## Methodology

### 1. Data Engineering

- Importing and organizing vibration recordings.
- Standardizing sampling frequencies.
- Preparing recording metadata.
- Segmenting signals for downstream analysis.
- Validating the processed dataset.

### 2. Digital Signal Processing

- Butterworth bandpass filtering.
- Fast Fourier Transform (FFT).
- Power Spectral Density (PSD) using Welch's method.
- Finite Impulse Response (FIR) moving-average analysis.
- Time-domain and frequency-domain signal analysis.

### 3. Feature Engineering

The analysis extracts statistical and spectral characteristics, including RMS, standard deviation, kurtosis, skewness, crest factor, dominant frequency, spectral centroid, spectral entropy, and spectral power.

Additional harmonic-frequency features are developed for motor load classification.

## Machine Learning Results

| Outcome                          | Model                             | Evaluation Metric | Result           |
| -------------------------------- | --------------------------------- | ----------------- | ---------------- |
| Bearing Condition Classification | Random Forest                     | Group CV Accuracy | **93.48%** |
| Bearing Defect Size Estimation   | XGBoost Regressor                 | Holdout R²       | **0.9563** |
| Motor Load Classification        | Random Forest + Harmonic Features | Group CV Accuracy | **97.20%** |

The reported results correspond to different prediction tasks and evaluation procedures and should not be interpreted as directly interchangeable performance measures.

### Outcome 1 — Bearing Condition Classification

A Random Forest classifier distinguishes four bearing conditions: Normal, Inner Race Fault, Ball Fault, and Outer Race Fault.

### Outcome 2 — Bearing Defect Size Estimation

An XGBoost regression model estimates bearing defect size using vibration-derived features.

### Outcome 3 — Motor Load Classification

A Random Forest classifier uses harmonic-frequency features extracted from vibration signals to identify motor operating loads.

## Repository Structure

```text
Bearing-analytical-set/
├── notebooks/
│   ├── 1_preprocessing.ipynb
│   ├── 2_signal_processing.ipynb
│   ├── 3_feature_engineering.ipynb
│   ├── 4_outcome_1_condition.ipynb
│   ├── 5_outcome_2_defect_size.ipynb
│   ├── 6_outcome_3_motor_load.ipynb
│   ├── 7_outcome_3_harmonic_rf.ipynb
│   └── 8_final_model_evaluation.ipynb
├── data/
├── outputs/
├── presentation/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Astaqhoffi01/Bearing-analytical-set.git
cd Bearing-analytical-set
```

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Open the notebooks using Jupyter Notebook or VS Code.

**Note:** The original CWRU recordings must be obtained separately. Notebook input paths and generated intermediate files may need to be configured before reproducing the experiments.

## Research Limitations

- Results are based on the selected CWRU recordings and experimental operating conditions.
- Model generalization to other machines, sensors, and real-world environments has not been established.
- Group-based validation is used for the classification experiments to reduce recording-level data leakage.
- Further external validation and robustness testing are recommended.

## Applications

- Predictive Maintenance
- Industrial Condition Monitoring
- Bearing Fault Diagnosis
- Vibration Signal Analytics
- Machine Learning for Industrial Systems

## Author

**Astaqhoffi Sabill**

Project Repository: [Bearing-analytical-set](https://github.com/Astaqhoffi01/Bearing-analytical-set)

## Acknowledgment

The vibration dataset is provided by the Case Western Reserve University Bearing Data Center.
