# FIFA World Cup 2026 Match Prediction

A machine learning project for predicting **2026 FIFA World Cup group-stage match scores and outcomes** using historical international football data, Elo ratings, recent team form, and multiple regression models.

Although another project in this repository also uses football data, this project has a different objective and workflow: it predicts **goal scores for a specific tournament** and then converts those predicted scores into match outcomes.

## Project Highlights

The notebook combines multiple data sources:

- historical international match results;
- the 2026 World Cup group-stage schedule;
- FIFA ranking information;
- international Elo ratings;
- 2026 World Cup match/team data.

It engineers features such as:

- pre-match Elo ratings;
- Elo difference;
- recent goals scored and conceded;
- recent points/form;
- days since the previous match;
- neutral/home-country indicators;
- year and tournament context.

## Models Compared

The project evaluates:

- Poisson Regression
- Dummy Regressor baseline
- Ridge Regression
- K-Nearest Neighbors
- Random Forest Regressor
- Extra Trees Regressor
- Tuned Extra Trees with `TimeSeriesSplit` and `GridSearchCV`
- HistGradientBoosting with Poisson loss

## Evaluation

The project evaluates both goal prediction and the match result derived from the predicted scores.

Metrics include:

- home/away MAE;
- home/away RMSE;
- R²;
- Poisson deviance;
- exact-score accuracy;
- match-result accuracy;
- weighted precision, recall, and F1-score.

In the saved notebook run, **Extra Trees** achieved a match-result accuracy of about **55.1%**, while the HistGradientBoosting model produced a weighted F1-score of about **55.8%**.

These are saved results from this project run, not guarantees for future data.

## 2026 Predictions

The generated prediction file is included at:

```text
outputs/world_cup_2026_predictions.csv
```

It contains 72 group-stage match rows and prediction columns for:

- Ridge Regression
- Random Forest
- Extra Trees
- HistGradientBoosting with Poisson loss

## Datasets

The datasets used by this project are kept outside GitHub and are available in the shared OneDrive folder:

**[Open the World Cup / selected-exercises dataset folder on OneDrive](https://1drv.ms/f/c/00b09ae9462395ef/IgD_Wa_VhP2lTohStq4OCs8RARNpYtzCSqS5FUa_oCMkBVk?e=8hMsA2)**

The project combines multiple football data sources, including historical international results, the 2026 World Cup schedule, FIFA ranking information, Elo ratings, and 2026 tournament team/match files.

Place the required files locally under the project's `data/` directory using the folder structure described in `data/README.md`.

The input datasets are not committed directly to GitHub so the repository remains lightweight while the project structure stays reproducible.

## Small GitHub-Ready Fixes

The original project has intentionally been preserved. Only a few small fixes were made:

- added a clear project title;
- removed one exact duplicated Elo-feature cell;
- removed a saved local-computer path from notebook output;
- fixed two accidental assignments that overwrote the historical `results` dataframe;
- moved the generated prediction CSV into `outputs/`;
- added README and dependency files.

The feature engineering, models, evaluation logic, tuning workflow, and prediction approach were otherwise left unchanged.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Then open:

```text
world_cup_2026_prediction.ipynb
```

## Project Structure

```text
03-world-cup-2026-prediction/
├── README.md
├── requirements.txt
├── world_cup_2026_prediction.ipynb
├── data/
│   └── README.md
└── outputs/
    └── world_cup_2026_predictions.csv
```
