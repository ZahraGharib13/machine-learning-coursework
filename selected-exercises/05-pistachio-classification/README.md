# Pistachio Classification

A selected machine learning exercise for classifying two pistachio varieties from geometric and shape measurements.

## What the Notebook Covers

- correlation analysis;
- removal of highly correlated features;
- stratified train/validation splitting;
- StandardScaler + K-Nearest Neighbors;
- weighted F1-score evaluation;
- mutual-information feature ranking;
- `SelectKBest`;
- 5-fold stratified cross-validation;
- repeated stratified cross-validation;
- interaction-feature experiments;
- log-transform experiments;
- final training and test prediction.

## Saved Results

The original notebook reports:

- baseline weighted F1: **0.8453**
- weighted F1 after removing highly correlated columns: **0.8597**
- 5-fold CV mean weighted F1 with feature selection: approximately **0.8567**

The final simple reduced-feature KNN model keeps the original coursework choice.

## Dataset

The training dataset for this exercise is available in the shared OneDrive folder:

**[Selected Exercises datasets on OneDrive](https://1drv.ms/f/c/00b09ae9462395ef/IgD_Wa_VhP2lTohStq4OCs8RARNpYtzCSqS5FUa_oCMkBVk?e=8hMsA2)**

For this project, download:

```text
pistachio_train.csv
```

After downloading, rename `pistachio_train.csv` to `train.csv` before placing it in the project's `data/` folder.

The notebook expects the local training file at:

```text
data/train.csv
```

The original assignment workflow also references:

```text
data/test.csv
```

The shared OneDrive folder contains the **training datasets used for model development and validation**. The test file is only needed if you want to reproduce the final assignment submission-generation step.

The dataset is kept outside GitHub so the repository stays lightweight and the original data files are not duplicated across projects.

## Important Fix

The original notebook saved only the fitted `KNeighborsClassifier`, while the final predictions also depended on a separately fitted `StandardScaler`.

The GitHub-ready version saves the **complete scaler + KNN pipeline**, so the exported model contains the preprocessing required for inference.

Other modeling and feature-exploration choices were preserved.

## Project Structure

```text
05-pistachio-classification/
├── README.md
├── requirements.txt
├── pistachio_classification.ipynb
├── data/
│   └── README.md
└── outputs/
    └── README.md
```
