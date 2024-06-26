import logging
import json
import requests


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("logs.log", mode= "a")
formatter = logging.Formatter("INFO:root:Request time: %(asctime)s")
fh.setFormatter(formatter)
logger.addHandler(fh)


def get_users():
    logger.info("")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users_data = response.json()

    with open("users.json", "w") as file:
        json.dump(users_data, file, indent=4)

get_users()