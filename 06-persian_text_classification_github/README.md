# Persian Webpage Topic Classification

Multi-class classification of Persian webpages using TF-IDF features and a linear SVM (`LinearSVC`).

The project focuses on a practical, fast text-classification pipeline rather than computationally expensive tokenization. The final model uses lightweight Persian normalization, word-level TF-IDF n-grams, and `LinearSVC`.

## Results

| Model | Validation Weighted F1 | Validation Macro F1 |
|---|---:|---:|
| Text + URL + domain (tuned classifier) | 0.7971 | — |
| **Text only** | **0.8167** | **0.7215** |

The text-only model performed best and was selected as the final pipeline. It improved weighted F1 by about **0.0197 absolute** over the tuned richer-feature model while being simpler and faster.

## Dataset

The training set contains **4,789 labeled rows** across **22 categories**. The test set contains **417 rows**.

The dataset files are not included in this repository. To run the notebook, place these files in the project root:

```text
yektanet_train.csv
yektanet_test.csv
```

Expected input fields include:

- `description`
- `text_content`
- `title`
- `h1`
- `h2`
- `url`
- `domain`

The target column is `category`.

## Approach

### Lightweight Persian normalization

The text pipeline:

- normalizes common Arabic/Persian character variants,
- removes diacritics,
- converts zero-width non-joiners to spaces,
- replaces numeric sequences with a shared `NUM` token,
- normalizes whitespace.

A heavier Persian tokenizer was tested during experimentation but was not kept because of its substantially higher runtime.

### Text representation

The final model combines the main text fields and applies `TfidfVectorizer` with:

- word n-grams: `(1, 2)`
- `min_df=2`
- `max_df=0.98`
- `max_features=30000`
- sublinear term frequency

### Classifier

`LinearSVC` was chosen because it works well with high-dimensional sparse TF-IDF features and is fast enough for iterative experimentation.

A small grid search was also used for the richer text + URL + domain representation, tuning:

- `C`
- `class_weight`

The official model-selection metric is weighted F1.

## Why the simpler model won

The richer pipeline added:

- character n-grams from URLs,
- one-hot encoded domains.

Those features did not improve the validation result. The text-only model reached **0.8167 weighted F1**, compared with **0.7971** for the tuned richer-feature model.

This is a useful result: more features did not automatically produce a better model.

## Repository structure

```text
.
├── persian_text_classification.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

## Run locally

Create and activate a virtual environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

Place the two CSV files in the repository root and open:

```text
persian_text_classification.ipynb
```

Run the notebook from top to bottom.

The notebook can generate `submission.csv`, but generated outputs and dataset files are excluded from Git tracking.

## Reproducibility

The train/validation split and model use:

```python
random_state=42
```

The validation split is stratified to preserve the class distribution.

## Possible future improvements

If more compute is available, reasonable next experiments include:

- a small search over TF-IDF settings,
- character n-grams on selected text fields,
- calibrated linear classifiers,
- stronger error analysis on minority classes.

The current repository intentionally keeps the workflow lightweight and reproducible.
