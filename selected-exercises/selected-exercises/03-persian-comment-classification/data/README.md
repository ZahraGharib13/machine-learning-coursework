# Dataset

The input files are not included in this repository.

## Required files

```text
train.csv
test.csv
```

Place both files in this folder.

The notebook expects:

```python
pd.read_csv("data/train.csv")
pd.read_csv("data/test.csv")
```

The labeled training file must contain at least:

- `comment`
- `price_value`

The test file must contain a `comment` column.

Add a public source link here only after the original dataset source and redistribution rules are confirmed.
