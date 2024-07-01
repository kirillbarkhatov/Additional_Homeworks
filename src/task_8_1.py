import pandas as pd
import json

def avg_age_by_gender(df):
    avg_age_male = df[df['Sex'] == 'male']['Age'].mean()
    avg_age_female = df[df['Sex'] == 'female']['Age'].mean()
    result_dict = {'Мужчины': avg_age_male, 'Женщины': avg_age_female}
    return json.dumps(result_dict, ensure_ascii=False)


df = pd.read_csv("data/titanic.csv")

# sex_df = df.groupby(by="Sex").agg("Age").mean()
#
# result = {'Мужчины': float(sex_df.male), 'Женщины': float(sex_df.female)}
#
# print(result)
#
# print(avg_age_by_gender(df))
#
#
# age_df = df.loc[((df.Age > 50) & (df.Sex == "male")) | ((df.Age < 30) & (df.Sex == "female"))]
#
# print(age_df.to_json())
# def filter_age(df):
#     age_df = df.


avg_ticket = df.groupby(by="Pclass").agg("Fare").mean()
print(avg_ticket)


def fare_per_passenger_by_class(df):
    total_fare_by_class = df.groupby('Pclass')['Fare'].sum()
    total_passengers_by_class = df.groupby('Pclass')['PassengerId'].count()
    avg_fare_per_passenger_by_class = total_fare_by_class / total_passengers_by_class
    result_dict = avg_fare_per_passenger_by_class.to_dict()
    return json.dumps(result_dict)
print(fare_per_passenger_by_class(df))

