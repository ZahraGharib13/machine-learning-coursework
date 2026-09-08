# Football Match Outcome Classification

Machine Learning Homework 2: a multi-class classification project for predicting football match outcomes.

The target variable is `match_result`, with three classes:

- `home`
- `away`
- `draw`

## What the notebook covers

- exploratory data analysis;
- missing-value analysis;
- duplicate detection and removal;
- feature engineering from recent match history;
- date-based and form-based features;
- separate preprocessing for tree and non-tree models;
- class-aware train/test splitting;
- model comparison with classification metrics;
- confusion matrices.

## Models

The notebook includes:

- Dummy Classifier baseline
- Decision Tree Classifier
- Random Forest Classifier
- Logistic Regression
- K-Nearest Neighbors
- Linear SVC

## Dataset

The dataset is kept outside GitHub and is available in the shared OneDrive folder for the first two main machine learning projects:

**[Open the dataset folder on OneDrive](https://1drv.ms/f/c/00b09ae9462395ef/IgDF_niFZM4WQogg-Ci68gokAcyMT8GtkVCVHELylVwi7bQ?e=MNJO25)**

For this project, use the football match dataset and place it locally at:

```text
data/student_version2.csv
```

The notebook loads it with:

```python
pd.read_csv("data/student_version2.csv")
```

The data is not committed directly to the repository so the project remains lightweight.

## Evaluation

The notebook evaluates classification models using:

- Accuracy
- Weighted Precision
- Weighted Recall
- Weighted F1-score
- Log Loss, when probability estimates are available
- Classification reports
- Confusion matrices

`LinearSVC` does not expose `predict_proba()`, so the GitHub version reports its classification metrics without log loss.

## Small Fixes Made for GitHub

The original homework has intentionally been preserved. Only a few necessary fixes were made:

- changed the dataset path to a relative path;
- fixed Logistic Regression prediction-variable names;
- removed the invalid `LinearSVC.predict_proba()` call;
- corrected the SVC confusion-matrix title;
- added README and dependency files.

The feature engineering, preprocessing choices, train/test split, model choices, and overall workflow were otherwise left unchanged.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then open:

```text
football_match_outcome_classification.ipynb
```

## Project Structure

```text
02-football-match-outcome-classification/
├── README.md
├── requirements.txt
├── football_match_outcome_classification.ipynb
└── data/
    └── README.md
```

## Reproducibility Note

Several later model cells in the saved coursework notebook were not executed. Run the notebook locally with the original dataset to generate the full model comparison and final metrics.
