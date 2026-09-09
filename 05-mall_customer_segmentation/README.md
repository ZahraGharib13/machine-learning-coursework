# Mall Customer Segmentation

An unsupervised machine-learning project that segments mall customers using **K-Means clustering**.

## Dataset

The dataset contains 200 customers with the following original features:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

Dataset download: https://1drv.ms/f/c/00b09ae9462395ef/IgA7AJ6vdt3JQL3-g0HdaOX4AbekO4nQ9HSVbRfplJxOhbE?e=sJl17J

> The dataset itself is not included in this repository. Download it from the link above and save it as `mall_customers.csv` next to the notebook before running the project.

## Approach

The notebook performs:

1. Basic exploratory data analysis
2. Duplicate and missing-value checks
3. Feature engineering inside a reusable `Preprocessor` class
4. CustomerID removal
5. Gender encoding
6. Spending-level and income-level features
7. Income-spending and age-spending interaction features
8. K-Means clustering for multiple values of `k`
9. Silhouette-score comparison and silhouette plots
10. Final model training and submission generation

## Result

The best clustering result in the notebook is:

- **Best k:** 2
- **Silhouette score:** 0.6561

## Project Structure

```text
mall_customer_segmentation/
├── mall_customer_segmentation.ipynb
├── preprocessor.py
├── requirements.txt
├── .gitignore
└── README.md
```

The notebook also generates the submission artifacts required by the assignment:

- `model`
- `submission.csv`
- `result.zip`

## Installation

```bash
pip install -r requirements.txt
```

Then launch Jupyter:

```bash
jupyter notebook
```

Open `mall_customer_segmentation.ipynb` and run the cells in order.

## Notes

All preprocessing and feature engineering used for clustering are implemented in `Preprocessor`, so the same transformation can be reproduced outside the notebook.
