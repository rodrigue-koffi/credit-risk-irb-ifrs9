# credit-risk-irb-ifrs9
End-to-end credit risk modelling pipeline implemented in Python, covering regulatory, accounting, and risk management perspectives.

This project demonstrates the full credit risk chain from data preparation to capital assessment, including IRB, IFRS9, Monte Carlo simulation, and reverse stress testing.

---

## Project Overview

This repository implements a complete credit risk framework including:

- Probability of Default (PD) modelling
- Loss Given Default (LGD) estimation
- Exposure at Default (EAD)
- Expected Loss (EL)
- IFRS9 Expected Credit Loss (ECL)
- Basel IRB Capital calculation
- Monte Carlo economic capital simulation
- Reverse stress testing

The goal is to showcase an end-to-end, production-style credit risk pipeline.

---

## Pipeline Architecture

1. Data loading and governance  
2. Preprocessing and feature preparation  
3. PD modelling (logistic regression)  
4. Model validation (AUC, Gini, KS)  
5. LGD estimation (Basel proxy)  
6. EAD estimation  
7. Expected Loss calculation  
8. IFRS9 Expected Credit Loss  
9. Basel IRB Capital calculation  
10. Monte Carlo loss simulation  
11. Portfolio reporting  
13. Reverse stress testing  

---

## Model Performance

The baseline PD model achieves:

- AUC: ~0.64  
- Gini: ~0.28  
- KS: ~0.21  

The baseline model achieves a Gini of ~0.28, leaving room for improvement through feature engineering.

---

## Portfolio Results (Example Output)

- Average PD: ~30%  
- Expected Loss: ~531  
- IFRS9 ECL: ~638  
- Average IRB Capital: ~580  

Monte Carlo simulation provides an empirical loss distribution and tail risk metrics.

---

## Reverse Stress Testing

The reverse stress module identifies portfolio breakpoints.

Example result:

> Portfolio break point estimated at an average PD of ~60%

This provides a simplified ICAAP-style resilience analysis.

---

## Methodology

- Logistic regression PD model  
- Basel-inspired LGD proxy  
- Credit amount proxy for EAD  
- TTC to PIT approximation for IFRS9  
- Gaussian copula-inspired IRB capital formula  
- Monte Carlo loss simulation  
- Scenario-based reverse stress testing  

---

## Tech Stack

- Python  
- NumPy / Pandas  
- Scikit-learn  
- SciPy  

---

## Purpose

This project is designed to:

- Demonstrate credit risk modelling skills  
- Illustrate regulatory concepts (Basel & IFRS9)  
- Provide a structured, production-style pipeline  
- Showcase quantitative risk engineering capabilities  

---

## Possible Improvements

- Feature engineering for higher Gini  
- PIT macroeconomic modelling  
- Lifetime ECL staging (IFRS9 stages 1–3)  
- Downturn LGD modelling  
- Economic capital optimization  
- Visualization dashboards  

---

## Disclaimer

This project is for educational and demonstration purposes only and does not represent a production-grade banking model.

---

## Author

Credit risk quantitative modelling project developed for portfolio and learning purposes.
