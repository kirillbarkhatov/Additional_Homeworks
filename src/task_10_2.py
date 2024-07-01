import pandas as pd


df = pd.read_csv("data/titanic.csv")
print(df.info())

class_df = df.groupby(by="Pclass").agg({
    "Fare": "mean",
    "PassengerId": "count"
}
)

class_df.columns = ['average_ticket_price', 'passenger_count']
class_df.reset_index(inplace=True)
rr = class_df.transpose()
rr.columns = ["1st", "2nd", "3rd"]
ff = rr.transpose()
ff = ff.drop('Pclass', axis=1)
# class_df.replace([1], "1st")
print(ff)



result_dict = ff.to_json(orient="index")
print(result_dict)