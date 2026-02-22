# Credit Risk IRB–IFRS9 End-to-End Pipeline

End-to-end credit risk modelling pipeline implemented in Python, covering regulatory (Basel), accounting (IFRS9), and internal risk (ICAAP) perspectives.

This project demonstrates a full credit risk chain from raw data to capital assessment and resilience analysis.

---

## Project Overview

This repository implements a complete credit risk framework including:

- Probability of Default (PD) modelling
- Loss Given Default (LGD) downturn estimation
- Exposure at Default (EAD) modelling
- Margin of Conservatism (MoC) concept
- Basel IRB Capital calculation
- Risk-Weighted Assets (RWA)
- IFRS9 Expected Credit Loss (ECL)
- Monte Carlo economic capital simulation
- Stress testing and reverse stress testing

The objective is to showcase a production-style, end-to-end credit risk modelling pipeline.

---

## Pipeline Architecture

### 1️ Data Foundations
- Data loading and governance checks
- Data preprocessing and feature preparation

### 2️ Default Risk Modelling
- TTC PD modelling (logistic regression)
- Model validation (AUC, Gini, KS)
- Point-in-Time calibration (IFRS9 proxy)

### 3️ Loss Parameters
- LGD downturn estimation
- Dynamic EAD modelling (credit amount proxy)
- Margin of Conservatism concept integration

### 4️ Basel Regulatory Layer
- Basel IRB capital calculation  
  (default correlation, 99.9% quantile)
- Risk-Weighted Assets (RWA) derivation

### 5️ IFRS9 Accounting Layer
- IFRS9 staging (Stage 1 / 2 / 3 classification)
- Expected Credit Loss (PD PIT × LGD × EAD)

### 6️ Internal Risk & ICAAP
- Stress testing concepts
- Monte Carlo loss simulation
- Tail risk metrics (VaR)

### 7️ Portfolio Resilience
- Risk reporting dashboard
- Reverse stress testing (portfolio breakpoints)

---

## Model Performance (Baseline)

Baseline PD model performance:

- AUC: ~0.64  
- Gini: ~0.28  
- KS: ~0.21  

The baseline model achieves a Gini of ~0.28, leaving room for improvement through feature engineering.

---

## Example Portfolio Outputs

Typical outputs produced by the pipeline:

- Average PD: ~30%  
- Expected Loss: ~531  
- IFRS9 ECL: ~638  
- Average IRB Capital: ~580  
- RWA derived from Basel capital

Monte Carlo simulation provides empirical loss distributions and tail risk indicators.

---

## Reverse Stress Testing

The reverse stress module identifies portfolio breakpoints by estimating the level of deterioration required to breach capital buffers.

Example output:

> Portfolio break point estimated at an average PD of ~60%

This provides a simplified ICAAP-style resilience analysis.

---

## Methodology

- Logistic regression PD model  
- Basel-inspired downturn LGD proxy  
- Credit amount proxy for EAD  
- TTC → PIT approximation for IFRS9  
- Basel IRB capital formula implementation  
- RWA derivation from regulatory capital  
- Monte Carlo loss simulation  
- Scenario-based reverse stress testing  

---

## Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- SciPy  

---

## Project Objectives

This project aims to:

- Demonstrate practical credit risk modelling skills  
- Bridge Basel and IFRS9 frameworks  
- Showcase end-to-end quantitative risk engineering  
- Provide a structured, production-style pipeline  

---

## Possible Improvements

- Feature engineering for higher PD performance  
- Full PIT macroeconomic modelling  
- IFRS9 lifetime ECL staging logic  
- Advanced downturn LGD modelling  
- Economic capital optimization  
- Interactive dashboards

---

## Disclaimer

This project is for educational and demonstration purposes only and does not represent a production-grade banking model.

---

## Author

# Rodrigue KOFFI

**Quantitative Risk Analyst**  
Credit Risk (IFRS 9) & Market Risk  
FRM Level I Candidate<br>
🔗 LinkedIn: https://www.linkedin.com/in/rodrigue-k-011aa01b8
