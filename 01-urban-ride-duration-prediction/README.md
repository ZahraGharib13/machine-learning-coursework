# Urban Ride Duration Prediction

Machine Learning Homework 1: a regression project for predicting urban ride duration (`elapsed_seconds`) from trip information, coordinates, and engineered time/distance features.

## What the notebook covers

- exploratory data analysis;
- basic data cleaning and outlier checks;
- feature engineering from timestamps and coordinates;
- one-hot encoding of categorical features;
- comparison of regression models;
- MAE and RMSE evaluation;
- Random Forest feature importance.

The notebook compares:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- K-Nearest Neighbors Regressor

## Dataset

The dataset is kept outside GitHub and is available in the shared OneDrive folder for the first two main machine learning projects:

**[Open the dataset folder on OneDrive](https://1drv.ms/f/c/00b09ae9462395ef/IgDF_niFZM4WQogg-Ci68gokAcyMT8GtkVCVHELylVwi7bQ?e=MNJO25)**

For this project, use the ride-duration dataset and place it locally at:

```text
data/student_version.csv
```

The notebook loads it with:

```python
pd.read_csv("data/student_version.csv")
```

The data is not committed directly to the repository so the project remains lightweight.

## Reported Results

This is a **regression** problem, so accuracy is not the appropriate evaluation metric.

The original notebook compares models using:

- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)

In the saved notebook results, the best-performing Random Forest configuration reported:

- **MAE:** 181.75 seconds
- **RMSE:** 296.24 seconds

These values are reported from the original coursework run. Because the dataset is not publicly available, other users cannot reproduce the results without authorized access to the same data.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then open:

```text
urban_ride_duration_prediction.ipynb
```

## Notes on the GitHub version

The original coursework notebook has intentionally been preserved with only small GitHub-ready fixes:

- the dataset path was changed to a relative path;
- the old author line was removed;
- the feature-importance cell was corrected to use the Random Forest model that the notebook identifies as the best-performing RF configuration.

The original modeling workflow, analysis, model choices, and saved notebook outputs were otherwise kept intact.

## Project Structure

```text
01-urban-ride-duration-prediction/
├── README.md
├── requirements.txt
├── urban_ride_duration_prediction.ipynb
└── data/
    └── README.md
```
