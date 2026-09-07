# Dataset

The input datasets are not included in this repository.

## Required files

```text
fraud_train.csv
fraud_test.csv
```

Place them locally in this folder.

The training dataset in the saved notebook contains **7,840 rows and 31 columns** before duplicate removal, with a strongly imbalanced target:

```text
Class 0: 7,471
Class 1:   369
```

The notebook loads the files with:

```python
pd.read_csv("data/fraud_train.csv")
pd.read_csv("data/fraud_test.csv")
```

Add a source link here only after the original public source and redistribution rules are confirmed.
