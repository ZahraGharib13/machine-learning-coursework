# Fraud Detection

A selected machine learning exercise for detecting fraudulent transactions in an imbalanced binary-classification dataset.

## What the Notebook Covers

- duplicate analysis and removal;
- class-imbalance inspection;
- correlation analysis;
- outlier investigation without blindly deleting informative fraud samples;
- train/validation split with stratification;
- scaling of `Time` and `Amount`;
- SVC classification;
- hyperparameter tuning with `RandomizedSearchCV`;
- stratified 5-fold cross-validation;
- F1-score evaluation;
- final retraining on all labeled data;
- test prediction and model export.

## Model

The final approach uses an `SVC` model inside a scikit-learn `Pipeline`.

The hyperparameter search explores:

- `C`
- `gamma`
- class weighting
- RBF kernel

## Saved Results

In the original notebook run:

- best cross-validation F1: **0.9879**
- validation F1: **0.9930**

The best saved hyperparameters were approximately:

```text
C = 85.69
gamma = 0.000153
kernel = rbf
class_weight = None
```

These are results from the saved coursework run. The unlabeled test set does not provide a test F1-score.

## Dataset

The datasets are not included in this repository.

Required local files:

```text
fraud_train.csv
fraud_test.csv
```

Place them here:

```text
05-fraud-detection/
├── fraud_detection.ipynb
└── data/
    ├── README.md
    ├── fraud_train.csv
    └── fraud_test.csv
```

The notebook uses relative paths:

```python
pd.read_csv("data/fraud_train.csv")
pd.read_csv("data/fraud_test.csv")
```

## Small GitHub-Ready Fixes

The original exercise has intentionally been preserved. Only necessary fixes were made:

- changed dataset paths to relative paths;
- moved generated files into `outputs/`;
- fixed model serialization so the **complete fitted preprocessing + SVC pipeline** is saved instead of only the SVC step;
- fixed the final artifact-packaging cell so it no longer references an unrelated notebook filename;
- added README and dependency files.

The EDA, outlier reasoning, SVC model, randomized search, validation workflow, and final training strategy were otherwise left unchanged.

## Setup

```bash
pip install -r requirements.txt
```

Then open:

```text
fraud_detection.ipynb
```

## Generated Outputs

After running the notebook with the original data:

```text
outputs/
├── submission.csv
├── fraud_detection_pipeline.joblib
└── model_artifacts.zip
```

## Project Structure

```text
05-fraud-detection/
├── README.md
├── requirements.txt
├── fraud_detection.ipynb
├── data/
│   └── README.md
└── outputs/
    └── README.md
```
