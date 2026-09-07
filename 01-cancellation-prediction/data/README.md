# Dataset

The input data is not included in this repository.

## Required files

```text
train_data.csv
test_data.csv
```

Place them in this folder:

```text
data/
├── README.md
├── train_data.csv
└── test_data.csv
```

The notebook expects the relative paths:

```python
pd.read_csv("data/train_data.csv")
pd.read_csv("data/test_data.csv")
```

The saved coursework notebook shows:

- training data: 101,017 rows and 22 columns before duplicate removal;
- test data: 43,293 rows and 20 columns.

Add a public source link here only if the dataset's original source and redistribution/access rules are confirmed.
