import pandas as pd


def filt_sort_df(df):
    age_df = df.loc[((df.Age < 30) & (df.Fare > 50))].sort_values(by="Name")
    return age_df


df = pd.read_csv("data/titanic.csv")
print(filt_sort_df(df))
