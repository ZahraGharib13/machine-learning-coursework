# MrBilit Search Data Analysis

A compact exploratory data analysis (EDA) project based on real-world search logs from the MrBilit travel platform.

## What this project does

- Measures the relative popularity of travel service types.
- Normalizes destination strings by removing terminal/station suffixes after `-`.
- Finds the 20 most-searched cities.
- Maps searched cities to provinces and finds the 15 most-searched provinces.
- Compares search popularity with 2016 city population data.

## Dataset

**Dataset link:** [Dataset link]()

Expected local files:

- `mrbilit_search.json`
- `iran_cities.csv`

Place them in the same directory as the notebook before running it.

## Main results

Using the provided dataset:

- Bus searches account for about **40.24%** of all searches.
- Flight searches account for about **24.96%**.
- The most-searched cities start with **Tehran, Mashhad, Isfahan, Shiraz, and Ahvaz**.
- The most-searched provinces start with **Tehran, Razavi Khorasan, Khuzestan, Fars, and Hormozgan**.
- Cities above 500k population that were not in the top 20 searched cities: **Ardabil, Hamedan, Urmia**.

## Tech stack

- Python
- pandas
- Plotly

## Run

```bash
pip install -r requirements.txt
jupyter notebook search_analysis.ipynb
```

## Project structure

```text
.
├── search_analysis.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

## Notes

The raw datasets are intentionally not included in this repository. Add the dataset link above and keep the data files local.
