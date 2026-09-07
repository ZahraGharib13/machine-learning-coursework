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

The dataset is not included in this repository.

Place:

```text
train.csv
test.csv
```

inside the local `data/` folder.

## Important Fix

The original notebook saved only the fitted `KNeighborsClassifier`, while the final predictions also depended on a separately fitted `StandardScaler`.

The GitHub-ready version saves the **complete scaler + KNN pipeline**, so the exported model contains the preprocessing required for inference.

Other modeling and feature-exploration choices were preserved.

## Project Structure

```text
08-pistachio-classification/
├── README.md
├── requirements.txt
├── pistachio_classification.ipynb
├── data/
│   └── README.md
└── outputs/
    └── README.md
```
