
import numpy as np
import pandas as pd

class Preprocessor:
    def __init__(self, df):
        self.df = df.copy()

    def drop_customer_id(self):
        self.df.drop(columns=["CustomerID"], inplace=True)

    def handle_missing_values(self):
        self.df.fillna(0, inplace=True)

    def encode_gender(self):
        self.df["Gender"] = self.df["Gender"].map({
            "Male": 0,
            "Female": 1
        })

    def add_spending_level(self):
        self.df["Spending_Level"] = pd.cut(
            self.df["Spending Score (1-100)"],
            bins=[0, 30, 50, 70, 100],
            labels=[0, 1, 2, 3],
            include_lowest=True
        ).astype(int)

    def add_income_level(self):
        self.df["Income_Level"] = pd.cut(
            self.df["Annual Income (k$)"],
            bins=[0, 40, 70, 100, float("inf")],
            labels=[0, 1, 2, 3]
        ).astype(int)

    def add_income_spending_interaction(self):
        self.df["Income_Spending"] = (
            self.df["Annual Income (k$)"] *
            self.df["Spending Score (1-100)"]
        )

    def add_age_spending_interaction(self):
        self.df["Age_Spending"] = (
            self.df["Age"] *
            self.df["Spending Score (1-100)"]
        )

    def transform(self):
        self.drop_customer_id()
        self.handle_missing_values()
        self.encode_gender()
        self.add_spending_level()
        self.add_income_level()
        self.add_income_spending_interaction()
        self.add_age_spending_interaction()

        return self.df