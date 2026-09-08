# Persian Comment Classification

A selected machine learning exercise for predicting a binary `price_value` label from Persian-language comments.

What makes this exercise useful for a portfolio is that the classifier logic is implemented largely from scratch instead of relying on a ready-made Naive Bayes estimator.

## What the Notebook Covers

- stratified train/validation splitting;
- Persian text normalization with Hazm;
- tokenization and stop-word filtering;
- special handling for price-related word forms;
- class prior probabilities;
- per-class token-frequency counting;
- Laplace smoothing;
- Naive Bayes-style probability calculation;
- validation accuracy;
- retraining the token statistics on the full labeled dataset;
- prediction on an unlabeled test set.

## Saved Result

The original notebook reports:

```text
Validation accuracy: 0.83375
```

That is approximately **83.4% validation accuracy**.

The test file is unlabeled in the notebook, so no test accuracy is claimed.

## Dataset

The training dataset for this exercise is available in the shared OneDrive folder:

**[Selected Exercises datasets on OneDrive](https://1drv.ms/f/c/00b09ae9462395ef/IgD_Wa_VhP2lTohStq4OCs8RAZsYOLE0kHru3543HtPvgWk?e=JByTLx)**

For this project, download:

```text
commens_train.csv
```

After downloading, rename `commens_train.csv` to `train.csv` before placing it in the project's `data/` folder.

The notebook expects the local training file at:

```text
data/train.csv
```

The original assignment workflow also references:

```text
data/test.csv
```

The shared OneDrive folder contains the **training datasets used for model development and validation**. The test file is only needed if you want to reproduce the final assignment submission-generation step.

The dataset is kept outside GitHub so the repository stays lightweight and the original data files are not duplicated across projects.

## Important Fix Made

The original notebook had one real retraining bug.

After calculating new word counts from the **full training dataset**, it stored them in `negative_class_count` and `positive_class_count`. However, `compute_probability()` continued using the older `words_in_neg_class` and `words_in_pos_class` dictionaries created from only the training split.

This GitHub version updates the dictionaries that the prediction function actually uses, so the final test predictions now use statistics learned from the full labeled training set.

Other than that, the original preprocessing and hand-built Naive Bayes approach were preserved.

## Other Small GitHub-Ready Changes

- changed dataset paths to relative paths;
- moved the Hazm installation requirement to `requirements.txt`;
- saved the generated submission under `outputs/`;
- removed the assignment-specific ZIP cell that referenced a different notebook filename;
- added README and dependency files.

## Setup

```bash
pip install -r requirements.txt
```

Then open:

```text
persian_comment_classification.ipynb
```

## Generated Output

After running the notebook:

```text
outputs/
└── submission.csv
```

## Project Structure

```text
03-persian-comment-classification/
├── README.md
├── requirements.txt
├── persian_comment_classification.ipynb
├── data/
│   └── README.md
└── outputs/
    └── README.md
```
