# Machine Learning Coursework

A curated collection of machine learning projects and selected coursework implemented in Python.

This repository includes larger end-to-end projects as well as selected exercises that demonstrate different parts of the machine learning workflow, including data preprocessing, feature engineering, model comparison, validation, hyperparameter tuning, text classification, imbalanced classification, regression, and model export.

## Repository Structure

```text
machine-learning-coursework/
├── 01-urban-ride-duration-prediction/
├── 02-football-match-outcome-classification/
├── 03-world-cup-2026-prediction/
└── selected-exercises/
    ├── 01-cancellation-prediction/
    ├── 02-fraud-detection/
    ├── 03-persian-comment-classification/
    ├── 04-nba-5-year-career-prediction/
    ├── 05-pistachio-classification/
    └── 06-trip-reason-classification/
```

## Main Projects

| Project | Task | Highlights |
| --- | --- | --- |
| [Urban Ride Duration Prediction](01-urban-ride-duration-prediction/) | Regression | EDA, feature engineering, model comparison, Random Forest, Gradient Boosting, KNN |
| [Football Match Outcome Classification](02-football-match-outcome-classification/) | Multiclass classification | Football feature engineering, preprocessing pipelines, Logistic Regression, Random Forest, Decision Tree, KNN, Linear SVC |
| [FIFA World Cup 2026 Prediction](03-world-cup-2026-prediction/) | Score and match-outcome prediction | Historical international results, FIFA/Elo ratings, recent form, Poisson models, Random Forest, Extra Trees, time-aware tuning |

### 01 — Urban Ride Duration Prediction

A regression project for predicting ride duration from trip-related features.

The notebook includes exploratory analysis, cleaning, feature engineering, and comparison of several regression models such as Linear Regression, Decision Trees, Random Forest, Gradient Boosting, and KNN.

In the saved coursework run, the best reported Random Forest configuration achieved approximately:

- **MAE:** 181.75
- **RMSE:** 296.24

[View project](01-urban-ride-duration-prediction/)

### 02 — Football Match Outcome Classification

A multiclass classification project for predicting football match outcomes.

The project includes substantial football-specific feature engineering, such as recent scoring and conceding form, rating differences, rest days, availability-related features, and other match context.

Several classification models are explored, including:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Linear SVC

[View project](02-football-match-outcome-classification/)

### 03 — FIFA World Cup 2026 Prediction

A tournament-focused machine learning project for predicting scores and outcomes for the **2026 FIFA World Cup group stage**.

The workflow combines several football data sources, including historical international results, FIFA ranking information, Elo ratings, recent team form, and the 2026 tournament schedule.

Models explored include:

- Poisson Regression
- Ridge Regression
- KNN Regression
- Random Forest
- Extra Trees
- Tuned Extra Trees with `TimeSeriesSplit`
- HistGradientBoosting with Poisson loss

The project also generates predictions for the 2026 group-stage schedule.

[View project](03-world-cup-2026-prediction/)

---

## Selected Exercises

These smaller projects were selected from additional coursework because they demonstrate useful or distinct machine learning techniques.

| Exercise | Focus | Saved result / notable feature |
| --- | --- | --- |
| [Cancellation Prediction](selected-exercises/01-cancellation-prediction/) | Binary classification | CatBoost, early stopping, threshold tuning; validation F1 ≈ **0.954** |
| [Fraud Detection](selected-exercises/02-fraud-detection/) | Imbalanced classification | SVC, RandomizedSearchCV, stratified CV; validation F1 ≈ **0.993** |
| [Persian Comment Classification](selected-exercises/03-persian-comment-classification/) | Persian NLP | Naive Bayes-style classifier implemented largely from scratch; validation accuracy ≈ **83.4%** |
| [NBA 5-Year Career Prediction](selected-exercises/04-nba-5-year-career-prediction/) | Binary classification | Logistic Regression, feature engineering, ROC-AUC evaluation |
| [Pistachio Classification](selected-exercises/05-pistachio-classification/) | Binary classification | KNN, feature selection, mutual information, cross-validation; weighted F1 ≈ **0.860** |
| [Trip Reason Classification](selected-exercises/06-trip-reason-classification/) | Binary classification | Extra Trees, mixed preprocessing, date/route feature engineering; validation accuracy ≈ **87.2%** |

## Techniques Demonstrated

Across the repository, the projects cover:

- exploratory data analysis and data cleaning;
- numerical and categorical preprocessing;
- domain-specific feature engineering;
- regression and classification;
- imbalanced classification;
- text preprocessing for Persian-language data;
- train/validation/test workflows;
- stratified splitting and cross-validation;
- time-aware validation;
- hyperparameter search;
- decision-threshold tuning;
- feature selection and feature importance;
- scikit-learn pipelines;
- model serialization and reusable preprocessing.

## Technologies

The repository mainly uses:

- Python
- pandas
- NumPy
- scikit-learn
- CatBoost
- Hazm
- Jupyter Notebook

Additional dependencies for individual projects are listed in each project's `requirements.txt`.

## Datasets

Most input datasets are **not committed to the repository**.

Depending on the project, datasets may come from public datasets, Kaggle, official data sources, or university coursework resources. Some datasets may also have access or redistribution restrictions.

Each project contains a `data/README.md` describing:

- the required filenames;
- the expected local directory structure;
- how the notebook loads the data;
- source information when the original public source has been confirmed.

This keeps the repository lightweight while preserving reproducible project structure where dataset access permits it.

## Running a Project

Clone the repository:

```bash
git clone https://github.com/ZahraGharib13/machine-learning-coursework.git
cd machine-learning-coursework
```

Then enter the project you want to run and install its dependencies:

```bash
pip install -r requirements.txt
```

Place the required dataset files in that project's `data/` directory according to its `data/README.md`, then open the Jupyter notebook.

## Notes

This repository contains coursework and selected academic exercises. The projects have been organized for readability and portfolio presentation while preserving the original modeling approaches as much as possible. Small fixes were made only where needed for portability, reproducibility, or clear runtime issues.

For implementation details, dataset instructions, model notes, and saved results, see the README inside each project folder.
