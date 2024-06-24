import datetime


def one_week_delta(list_of_date):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    new_list_of_date = []
    for date in list_of_date:
        date_obj = datetime.datetime.strptime(date,"%Y.%m.%d")
        # print(date_obj)
        new_date = date_obj + datetime.timedelta(days=7)
#         print(new_date)
        result = f'{months[new_date.month - 1]} {new_date.day}, {new_date.year}'
#         print(result)
        new_list_of_date.append(result)
    return new_list_of_date


if __name__ in "__main__":
    list_of_date = ["2022.12.31", "2023.1.7"]
    print(one_week_delta(list_of_date))