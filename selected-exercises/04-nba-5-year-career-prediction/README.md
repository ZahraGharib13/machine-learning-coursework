# NBA 5-Year Career Prediction

A selected machine learning exercise for predicting whether an NBA player will remain in the league for at least five years.

The target column is:

```text
target_5yrs
```

## What the Notebook Covers

- duplicate inspection and removal;
- class-balance inspection;
- Logistic Regression baseline;
- feature engineering from player statistics;
- train/validation splitting with stratification;
- scaling;
- ROC-AUC evaluation;
- coefficient inspection;
- final retraining on all labeled data;
- probability predictions for the test set.

## Feature Engineering

The notebook creates additional features related to:

- playing time and role;
- scoring efficiency;
- shooting efficiency;
- assist-to-turnover ratio;
- rebounding activity;
- defensive contribution;
- all-around contribution;
- interaction features;
- threshold-based high-performance indicators.

## Important Fixes

The original exercise has intentionally been preserved. Only a few real issues were corrected:

- dataset paths were changed to relative paths;
- baseline ROC-AUC now uses predicted probabilities instead of hard class labels;
- the `starter_role_proxy` threshold is now learned from the training data instead of recalculating a median on validation/test data;
- the final model now uses the **same feature-engineering steps** that were used during validation;
- the saved model now includes both `StandardScaler` and Logistic Regression;
- generated files are saved under `outputs/`;
- the old assignment packaging cell no longer refers to a different notebook filename.

## Previous Saved Result

Before the small leakage/consistency fixes, the original notebook reported a feature-engineered ROC-AUC of approximately:

```text
0.7564
```

Because the corrected GitHub version changes two details of the evaluation pipeline, rerun the notebook locally to regenerate the corrected ROC-AUC. The README does not claim the old value as the final corrected score.

## Dataset

The datasets are not included in this repository.

Required files:

```text
nba_players_train.csv
nba_players_test.csv
```

Place them locally at:

```text
07-nba-5-year-career-prediction/
├── nba_5_year_career_prediction.ipynb
└── data/
    ├── README.md
    ├── nba_players_train.csv
    └── nba_players_test.csv
```

The notebook loads them with:

```python
pd.read_csv("data/nba_players_train.csv")
pd.read_csv("data/nba_players_test.csv")
```

## Setup

```bash
pip install -r requirements.txt
```

Then open:

```text
nba_5_year_career_prediction.ipynb
```

## Generated Outputs

After a full run:

```text
outputs/
├── submission.csv
├── nba_5yr_model.joblib
└── model_artifacts.zip
```

## Project Structure

```text
07-nba-5-year-career-prediction/
├── README.md
├── requirements.txt
├── nba_5_year_career_prediction.ipynb
├── data/
│   └── README.md
└── outputs/
    └── README.md
```
