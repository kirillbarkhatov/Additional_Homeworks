import datetime


def get_days_between_dates(start, end):
    st = datetime.datetime.strptime(start, "%d.%m.%Y")
    en = datetime.datetime.strptime(end, "%d.%m.%Y")
    return (en - st).days


print(get_days_between_dates("01.01.2022", "31.01.2022"))