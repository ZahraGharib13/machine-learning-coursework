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

The input files are not bundled.

Place:

```text
train_data.csv
test_data.csv
```

inside `data/`.

## GitHub-Ready Changes

The original modeling workflow was preserved. Only small repository-related changes were made:

- changed dataset loading to relative paths;
- saved the submission and fitted pipeline under `outputs/`;
- replaced the assignment-specific ZIP cell with artifact packaging that matches this project;
- added README and requirements files.

The feature engineering, Extra Trees model, validation split, and final training logic were otherwise left unchanged.

## Project Structure

```text
09-trip-reason-classification/
├── README.md
├── requirements.txt
├── trip_reason_classification.ipynb
├── data/
│   └── README.md
└── outputs/
    └── README.md
```
