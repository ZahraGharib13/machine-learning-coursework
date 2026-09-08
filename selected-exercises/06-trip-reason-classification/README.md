# Trip Reason Classification

A selected machine learning exercise for predicting a passenger's trip reason from booking and travel information.

The target is:

```text
TripReason
```

with the saved training labels `Work` and `Int`.

## What the Notebook Covers

- duplicate removal;
- stratified train/validation split;
- train-derived ID frequency features;
- missing-value handling;
- rare-category handling;
- vehicle-class imputation;
- Iranian holiday and weekend features;
- date/time feature engineering;
- cyclic encoding;
- route and destination frequency features;
- destination-region features;
- mixed numeric/categorical preprocessing with `ColumnTransformer`;
- Extra Trees classification;
- final retraining and model export.

## Saved Result

The original notebook reports:

```text
Validation accuracy: 0.87165
```

approximately **87.2%**.

The saved weighted F1-score is also approximately **0.87**.

## Dataset

The training dataset for this exercise is available in the shared OneDrive folder:

**[Selected Exercises datasets on OneDrive](https://1drv.ms/f/c/00b09ae9462395ef/IgD_Wa_VhP2lTohStq4OCs8RARNpYtzCSqS5FUa_oCMkBVk?e=8hMsA2)**

For this project, download:

```text
trip_train_data.csv
```

After downloading, rename `trip_train_data.csv` to `train_data.csv` before placing it in the project's `data/` folder.

The notebook expects the local training file at:

```text
data/train_data.csv
```

The original assignment workflow also references:

```text
data/test_data.csv
```

The shared OneDrive folder contains the **training datasets used for model development and validation**. The test file is only needed if you want to reproduce the final assignment submission-generation step.

The dataset is kept outside GitHub so the repository stays lightweight and the original data files are not duplicated across projects.

## GitHub-Ready Changes

The original modeling workflow was preserved. Only small repository-related changes were made:

- changed dataset loading to relative paths;
- saved the submission and fitted pipeline under `outputs/`;
- replaced the assignment-specific ZIP cell with artifact packaging that matches this project;
- added README and requirements files.

The feature engineering, Extra Trees model, validation split, and final training logic were otherwise left unchanged.

## Project Structure

```text
06-trip-reason-classification/
├── README.md
├── requirements.txt
├── trip_reason_classification.ipynb
├── data/
│   └── README.md
└── outputs/
    └── README.md
```
