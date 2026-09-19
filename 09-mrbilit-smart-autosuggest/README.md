# MrBilit Smart Auto-Suggest

A practical NLP/search-ranking project for generating ranked destination suggestions from partial or noisy user input.

The system handles:

- Persian prefix completion.
- English city names such as `Zahedan`.
- Wrong keyboard-layout input (English ↔ Persian).
- Misspellings using Levenshtein Edit Distance.
- Popularity-based ranking and fallback behavior.
- Five unique ranked suggestions per query.

## Benchmark

The submitted solution achieved:

**Mean RBO: 60.53**

The full-score threshold in the Quera evaluation was **30**.

> RBO (Rank-Biased Overlap) evaluates both item overlap and ranking order.

## Dataset

**Dataset link:** [Dataset link]()

Expected local files:

- `mrbilit_search.json`
- `iran_cities.csv`
- `typo_char.csv`
- `test_data.json`

Place them in the same directory as the notebook before running it.

## Ranking strategy

The `suggest()` function applies the following priority:

1. Direct Persian/original prefix match.
2. English city-name prefix match.
3. English-keyboard-to-Persian conversion.
4. Persian-keyboard-to-English conversion.
5. Levenshtein Edit Distance.
6. Search frequency as a tie-breaker/fallback ranking signal.

The original `AcceptString` is retained as the final label, so suggestions can include terminal-specific destinations when appropriate.

## Tech stack

- Python
- pandas
- python-Levenshtein
- Jupyter

## Run

```bash
pip install -r requirements.txt
jupyter notebook auto_suggest.ipynb
```

Running the final cells creates:

```text
submission.csv
```

with columns `Suggestion0` through `Suggestion4`.

## Project structure

```text
.
├── auto_suggest.ipynb
├── README.md
├── requirements.txt
```

## Notes

The raw datasets and generated submission are intentionally not committed.
Add the dataset URL to the placeholder above before publishing the repository.
