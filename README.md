# Kidney Disease Analysis

## Overview
This repository contains a Python analysis script for evaluating kidney disease stages based on Age, eGFR (Estimated Glomerular Filtration Rate), and Gender. The code segments the stages of kidney diseases and visualizes the distribution of these stages in a dataset.
## Note: According to https://www.mdapp.co/egfr-calculator-by-ckd-epi-79/ creatinine has been calculated.


## Data
The analysis is performed on a dataset (not provided in this repo) containing the following key columns:
- `age`: Age of the patient.
- `egfr`: Estimated Glomerular Filtration Rate.
- `sex`: Gender of the patient.

## Features
- Calculation of creatinine levels based on age, eGFR, and gender.
- Classification of eGFR levels into various categories of kidney health.
- Categorization of kidney disease stages based on creatinine levels.
- Visualization of the distribution of kidney disease stages.

## Usage
To run the script, ensure you have a dataset in CSV format. The main script `kidney_disease_analysis.py` reads the dataset, performs calculations, categorizations, and produces visualizations.

## Requirements
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- sksurv
- sklearn
- lifelines
- missingno
- plotly

## Installation
Install the required packages using

License: MIT
