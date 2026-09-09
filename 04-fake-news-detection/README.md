# Fake News Detection with Metadata and NLP Features

A machine-learning project for classifying news articles as **Fake** or **Real** using article metadata together with high-dimensional NLP text features.

## Project Highlights

- Combines structured metadata with NLP vectors.
- Uses date/time feature engineering.
- Uses frequency encoding for high-cardinality categorical features.
- Applies one-hot encoding during exploratory modeling.
- Reduces 42,141 text features to 200 components with PCA.
- Uses `SimpleImputer` and `StandardScaler`.
- Trains a linear Support Vector Classifier (`SVC`).
- Detects and investigates a target-proxy feature instead of accepting an unrealistically perfect score.

## Dataset

The dataset files are not stored directly in this repository due to their size.

You can download all required dataset files from the following OneDrive folder:

**[Download the dataset from OneDrive](https://1drv.ms/f/c/00b09ae9462395ef/IgA7AJ6vdt3JQL3-g0HdaOX4AbekO4nQ9HSVbRfplJxOhbE?e=sJl17J)**

After downloading, place the following files in the same directory as the notebook:

- `news_train.csv`
- `news_train_text_vectors.npz`
- `news_test.csv`
- `news_test_text_vectors.npz`

The original shapes used in the notebook are:

- Training metadata: 1,500 rows
- Training text vectors: 1,500 × 42,141
- Test metadata: 346 rows
- Test text vectors: 346 × 42,141

After removing duplicate metadata rows from the training data, the modeling dataset contains 1,467 training samples.

## Workflow

```text
Load metadata + sparse NLP vectors
        ↓
Clean and align rows
        ↓
Handle missing text values
        ↓
Train / validation split
        ↓
Feature engineering on publication date
        ↓
Frequency encoding for author and site_url
        ↓
One-hot encode type for initial analysis
        ↓
PCA: 42,141 → 200 text components
        ↓
Imputation + scaling
        ↓
Linear SVC
        ↓
Target-proxy investigation
        ↓
Remove type from final portfolio model
        ↓
Balanced linear SVC
        ↓
Train final model on all transformed training samples
        ↓
Predict 346 test samples
```

## Target-Proxy Finding

The first linear SVC achieved an F1 score of **1.000**. That result was investigated rather than accepted at face value.

A cross-tabulation showed that the `type` field deterministically separated the labels in the training data:

- `bias` and `hate` mapped to `Real`
- `bs`, `conspiracy`, `fake`, `junksci`, and `satire` mapped to `Fake`

Because `type` effectively acts as a target proxy, it was excluded from the final portfolio model to obtain a more realistic estimate of generalization performance.

## Results

| Experiment | F1 |
| --- | ---: |
| Linear SVC with `type` | 1.000 |
| Linear SVC without `type` + balanced class weights | 0.850 |

For the final validation model without `type`:

- Accuracy: **0.80**
- Class 1 precision: **0.83**
- Class 1 recall: **0.87**
- Class 1 F1: **0.85**
- Macro F1: **0.77**

The final classifier uses:

```python
SVC(
    kernel="linear",
    C=1,
    class_weight="balanced"
)
```

## PCA

The NLP representation starts with **42,141 features**. PCA reduces it to **200 components**.

The 200 components retain approximately **37.4%** of the variance in the training text representation.

## Repository Structure

```text
fake-news-detection/
├── fake_news_detection.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Create a virtual environment and install the dependencies:

```bash
pip install -r requirements.txt
```

Then place the four dataset files next to `fake_news_detection.ipynb` and run the notebook from top to bottom.

## Reproducibility

The train/validation split uses:

```python
random_state=42
```

The notebook uses a stratified 80/20 split for model evaluation. After model selection, the transformed training and validation matrices are concatenated and the selected SVC is fit on all available transformed training samples.

## Submission Output

The notebook creates:

```text
submission.csv
model
result.zip
```

The prediction file contains exactly **346 rows** with one `label` column containing `Fake` or `Real`.

## Notes

The submission/export cell is retained because this project originated as a course assignment. For portfolio purposes, the key modeling result is the leakage-aware model that excludes `type`.
