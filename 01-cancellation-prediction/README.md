# Ticket Cancellation Prediction

A selected machine learning exercise for predicting whether a booked ticket will be cancelled.

This project is a **binary classification** task. It uses booking, trip, customer-frequency, route, price, and date/time features and trains a CatBoost classifier.

## What the Notebook Covers

- train/validation split with class stratification;
- missing-value handling;
- ID-frequency features learned from the training split;
- vehicle-class imputation;
- booking lead-time features;
- discount features;
- route-frequency and route-price features;
- Iranian holiday and weekend features;
- cyclic encoding of hour/day/month variables;
- CatBoost classification;
- early stopping;
- decision-threshold tuning for F1-score;
- retraining on the full training data;
- test prediction and model export.

## Evaluation

The coursework is evaluated using **F1-score**.

In the saved notebook run:

- best validation F1: **0.9537**
- selected probability threshold: **0.64**
- best CatBoost iteration: **537**

These values are the saved validation results from the original run. The private test labels are not available in the notebook, so no test-set F1 is claimed here.

## Dataset

The dataset is not included in this repository.

Required files:

```text
train_data.csv
test_data.csv
```

Place them locally at:

```text
01-cancellation-prediction/
├── ticket_cancellation_prediction.ipynb
└── data/
    ├── README.md
    ├── train_data.csv
    └── test_data.csv
```

The notebook reads them with relative paths:

```python
pd.read_csv("data/train_data.csv")
pd.read_csv("data/test_data.csv")
```

See [`data/README.md`](data/README.md) for details.

## Small GitHub-Ready Fixes

The original exercise has intentionally been preserved. Only a few necessary or presentation-level fixes were made:

- changed dataset loading to relative paths;
- replaced the in-notebook CatBoost installation command with `requirements.txt`;
- fixed a missing `()` in a display-only cell;
- fixed the final packaging cell, which referred to the template notebook name instead of the completed notebook;
- saved generated submission/model files under `outputs/`;
- added project documentation.

The feature engineering, model configuration, validation split, early stopping, threshold search, and final training strategy were otherwise left unchanged.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Then open:

```text
ticket_cancellation_prediction.ipynb
```

## Generated Outputs

After a full run, the notebook creates:

```text
outputs/
├── submission.csv
├── model.cbm
└── model_artifacts.zip
```

## Project Structure

```text
01-cancellation-prediction/
├── README.md
├── requirements.txt
├── ticket_cancellation_prediction.ipynb
├── data/
│   └── README.md
└── outputs/
    └── README.md
```
