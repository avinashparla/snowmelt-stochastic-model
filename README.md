<<<<<<< HEAD
# Stochastic Snowmelt Modeling Framework

This repository contains code and data supporting the study:

**"A Stochastic Extension of Temperature-Index Snowmelt Modeling for Probabilistic Runoff Estimation in a Himalayan Basin"**

## Overview

This study develops a stochastic extension of the classical temperature-index (degree-day) snowmelt model by incorporating:

- State-dependent variability
- Autoregressive (AR1) temporal persistence
- Temperature-triggered jump processes
- Monte Carlo simulation for uncertainty quantification

## Structure

- `data/processed/` → Basin-averaged temperature and model outputs  
- `notebooks/` → Full modeling workflow  
- `outputs/figures/` → Figures used in the paper  
- `outputs/tables/` → Statistical summaries  
- `paper/` → LaTeX manuscript  

## Reproducibility

Run notebooks in order:

1. `01_preprocessing.ipynb`
2. `02_modeling.ipynb`
3. `03_monte_carlo.ipynb`
4. `04_results_figures.ipynb`

## Data Sources

- ERA5 Reanalysis (ECMWF)
- SRTM DEM (NASA)

## License

MIT License
=======
# snowmelt-stochastic-model
Stochastic snowmelt modeling framework for probabilistic runoff estimation in a Himalayan basin
>>>>>>> 1954a09786502394cdd90c6b5925d6683fcbee06
