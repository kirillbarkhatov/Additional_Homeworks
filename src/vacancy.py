import requests

import datetime

import logging

import json

from src.config import BASE_URL


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"logs/logs.log", mode="a")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

def get_vacancies(query: str, exclude_words: list = [], url: str = BASE_URL) -> list:
    """ Получаем вакансии с HH.ru """


    logger.info("Запущен скрипт получения вакансий")

    try:
        if exclude_words != []:
            exclude_words_str = f" NOT {" NOT ".join(exclude_words)}"
            logger.info(f"Сформирован список слов-исключений {exclude_words_str}")
        else:
            exclude_words_str = ""
            logger.info("Слова-исключения для поиска не вводились")

        params = {
            "text": f"NAME:{query}{exclude_words_str}",
            "period": 1
        }
        response = requests.get(url,params=params)
        vacancies_data = response.json()
        logger.info("Запрос выполнен")
        vacancies_list = []
        for vacancy in vacancies_data['items']:
            vacancies_list.append(
                {
                    "name": vacancy["name"],
                    "salary": vacancy.get("salary"),
                    "url": vacancy["url"]
                }
            )
        logger.info("Выполнение скрипта завершено")
        return vacancies_list
    except Exception as ex:
        logger.error(f"Выполнение скрипта вызвало ошибку {ex}")

