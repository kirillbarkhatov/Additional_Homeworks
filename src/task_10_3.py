import pandas as pd
import json


df = pd.read_csv("data/titanic.csv")
print(df.info())

df = df.set_index("PassengerId", drop=True)
df = df.loc[df.Survived == 1]
print(df.head())


# print(df.to_json(orient="records"))



with open("data/titanic_surv.json", "w") as file:
    json.dump(df.to_dict(orient="records"), file, indent=4)


print(len(df.to_dict(orient="records")))