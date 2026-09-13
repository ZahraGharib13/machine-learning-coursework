# Social Profile Gender Classification

An educational machine-learning project that classifies the `gender` label from social-profile text and metadata.

The project is designed as a compact example of a **heterogeneous scikit-learn pipeline**: structured numerical/categorical features and multiple text representations are combined in one `ColumnTransformer`, then classified with `LinearSVC`.

## Validation result

The original notebook reported:

| Metric | Score |
|---|---:|
| Macro F1 | **0.9469** |
| Accuracy | **~0.95** |

The validation split used an 80/20 stratified split with `random_state=42`. Both target classes had equal support in the validation set, so weighted and macro F1 were effectively the same for that run.

## Features

The model uses:

- `fullname`
- `username`
- `biography`
- `follower_count`
- `following_count`
- `age`
- `is_business`
- `is_verified`
- `is_private`

## Pipeline

```text
follower_count ─┐
following_count ─┴─> median imputation → log1p → StandardScaler

age ────────────────> most-frequent imputation → OneHotEncoder

boolean flags ──────> most-frequent imputation

fullname ───────────> character TF-IDF, 2–5 grams
username ───────────> character TF-IDF, 2–5 grams
biography ──────────> word TF-IDF, 1–2 grams

all features ───────> LinearSVC
```

### Why character TF-IDF for names and usernames?

Names and usernames contain spelling variants, transliterations, abbreviations, digits, underscores, prefixes, and suffixes. Character n-grams capture these patterns even when the exact token was never seen during training.

### Why word TF-IDF for biography?

Biography text contains semantic words and short phrases. Word unigram and bigram features provide a simple and effective representation for this type of text.

## Repository structure

```text
07-social-profile-gender-classification/
├── social_profile_gender_classification.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── outputs/
└── artifacts/
```

## Running the project

1. Create a virtual environment.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Put the dataset files in `data/`:

```text
data/train_data.csv
data/test_data.csv
```

4. Open and run:

```text
social_profile_gender_classification.ipynb
```

Generated submissions are written to `outputs/` and are ignored by Git.

## What was cleaned up from the original notebook?

- moved missing-value handling into the preprocessing pipeline
- removed duplicated and unused preprocessing definitions
- removed duplicated imports
- added reproducibility with `random_state=42`
- added both macro and weighted F1 reporting
- added a confusion matrix
- removed competition-specific ZIP/export code
- prevented large pipeline representations from cluttering notebook output
- organized the notebook into clear EDA, preprocessing, training, evaluation, and inference sections
- moved data and generated outputs outside the notebook root workflow

## Responsible-use note

Gender is a sensitive personal attribute. This repository is an **educational classification exercise**, not a system for making decisions about individuals.

The model can learn cultural and linguistic patterns from names, usernames, and biography text. These patterns may reflect dataset bias and may not generalize across populations, languages, identities, or contexts. It should not be used for profiling, eligibility decisions, access control, hiring, advertising, or other consequential applications.

## Possible next step

A small search over the `C` parameter of `LinearSVC` is a reasonable low-cost extension. A large grid over all TF-IDF settings is intentionally avoided because it can increase runtime substantially for limited expected benefit.
