# Dataset

The input datasets are not included in this repository.

## Required files

```text
nba_players_train.csv
nba_players_test.csv
```

Place both files in this folder.

The target in the training data is:

```text
target_5yrs
```

It indicates whether the player remains in the NBA for at least five years.

The notebook expects:

```python
pd.read_csv("data/nba_players_train.csv")
pd.read_csv("data/nba_players_test.csv")
```

Add a public source link here only after the exact original dataset source and redistribution rules are confirmed.
