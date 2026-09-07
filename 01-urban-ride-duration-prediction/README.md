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

The dataset is **not stored in this GitHub repository**.

File name:

```text
student_version.csv
```

Course dataset source:

[Download `student_version.csv`](https://vc.kntu.ac.ir/pluginfile.php/180251/mod_assign/introattachment/0/student_version.csv?forcedownload=1)

The course website may require university authentication.

After downloading the file, place it locally here:

```text
01-urban-ride-duration-prediction/
├── urban_ride_duration_prediction.ipynb
└── data/
    ├── README.md
    └── student_version.csv
```

The notebook uses this relative path:

```python
pd.read_csv("data/student_version.csv")
```

This makes the project portable without committing the dataset itself.

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
