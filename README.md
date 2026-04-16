# ❄️ Stochastic Snowmelt Modeling in the Himalayas

## 📌 Overview

This repository presents a **stochastic extension of the temperature-index (degree-day) snowmelt model** developed for the **Chandra Basin (Western Himalayas)**.

The model integrates:

* State-dependent variability
* Autoregressive temporal persistence (AR(1))
* Temperature-triggered jump processes

to move beyond deterministic melt estimation toward **probabilistic hydrological modeling**.

---

## 🎯 Objectives

* Develop a stochastic snowmelt framework
* Quantify variability and extreme melt events
* Validate model behavior using **MODIS snow cover observations**
* Assess sensitivity to key stochastic parameters

---

## 📂 Repository Structure

```
snowmelt_stochastic_model/
│
├── data/
│   ├── raw/                # MODIS, ERA5 inputs
│   ├── processed/          # Basin-averaged datasets
│
├── notebooks/
│   ├── preprocessing.ipynb
│   ├── modeling.ipynb
│   ├── validation.ipynb
│
├── outputs/
│   ├── figures/            # All figures used in paper
│   ├── processed/          # NetCDF model outputs
│
├── paper/
│   ├── snow_melt_model.tex
│   ├── references.bib
│   ├── final_pdf/
│
├── README.md
└── .gitignore
```

---

## ⚙️ Methodology

### 1. Deterministic Model

Temperature-index (degree-day) formulation:
[
M_t = \mathrm{DDF} \cdot \max(T_t - T_0, 0)
]

---

### 2. Stochastic Extensions

#### 🔹 AR(1) Persistence

Captures temporal correlation in melt variability:
[
\epsilon_t = \phi \epsilon_{t-1} + \eta_t
]

#### 🔹 State-Dependent Variability

Variance scales with melt intensity:
[
\sigma_t = a \cdot M_t + b
]

#### 🔹 Temperature-Triggered Jumps

Extreme melt events activated under warm conditions.

---

### 3. Monte Carlo Simulation

* Ensemble generation of melt trajectories
* Probabilistic runoff estimation
* Uncertainty quantification

---

## 📊 Key Results

* Deterministic model captures **seasonal structure**
* Stochastic models reproduce:

  * Short-term variability
  * Extreme melt spikes
* Heavy-tailed melt distributions observed

---

## ✅ Validation (MODIS)

Model outputs are validated using **MODIS snow cover fraction**:

* Correlation (Deterministic): **r ≈ -0.698**
* Stochastic models improve:

  * Melt variability representation
  * RMSE performance

---

## 🔬 Sensitivity Analysis

Key parameters tested:

* **Persistence (ϕ):** controls temporal memory
* **Jump probability (p):** controls extreme events

Findings:

* Higher ϕ → smoother, persistent melt
* Higher p → more frequent extreme spikes

---

## 📈 Figures

Main figures include:

* Uncertainty bands (Monte Carlo)
* Model comparison panels
* Distribution (log-scale)
* Sensitivity experiments
* MODIS validation plots

---

## 📦 Data Sources

* ERA5 Reanalysis (temperature)
* MODIS Snow Cover (MOD10A1)
* SRTM DEM

---

## 🚀 Applications

* Probabilistic runoff forecasting
* Climate impact studies
* Risk assessment in snow-fed basins
* Hydrological extremes analysis

---

## 🧠 Key Contribution

This work embeds stochastic variability **directly within the snowmelt process**, enabling intrinsic representation of uncertainty rather than treating it as an external perturbation.

---

## 📄 Paper

Full paper available in:

```
paper/final_pdf/
```

---

## 🛠️ Requirements

* Python (xarray, numpy, matplotlib)
* LaTeX (for manuscript)

---

## 👤 Author

Avinash Parla

---

## 📌 Status

✔ Model complete
✔ Validation complete
✔ Sensitivity analysis complete
✔ Paper submission ready

---
