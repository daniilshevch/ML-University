import numpy as np
import pandas as pd
import seaborn as sns
class ZScoreCounter:
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
    def get_average_value(self):
        return self.df[self.column_name].mean()
    def get_standard_deviation(self):
        return self.df[self.column_name].std()
    def get_z_score(self):
         average = self.get_average_value()
         standard_deviation = self.get_standard_deviation()
         return self.df[self.column_name].apply(lambda value: np.abs(value - average) / standard_deviation)



df = sns.load_dataset("planets")
pd.set_option('display.max_columns', None)
print(df.head())
print(df.info())
print(df.isna().sum())
distance_z_score_counter = ZScoreCounter(df, "distance")
orbital_period_z_score_counter = ZScoreCounter(df, "orbital_period")
year_z_score_counter = ZScoreCounter(df, "year")
df["distance_z_score"] = distance_z_score_counter.get_z_score()
df["orbital_period_z_score"] = orbital_period_z_score_counter.get_z_score()
df["year_z_score"] = year_z_score_counter.get_z_score()
##df["average_z_score"] = (df["distance_z_score"] + df["orbital_period_z_score"] + df["year_z_score"]) / 3
def define_outliers(df):
    return df[df["average_z_score"] > 3]
df["average_z_score"] = df[["distance_z_score", "orbital_period_z_score", "year_z_score"]].mean(axis=1)
outliers = define_outliers(df)
print(df)
print(outliers)

