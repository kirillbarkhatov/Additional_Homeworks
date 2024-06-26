import json
import logging
import datetime

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"logs/logs.log", mode="a")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)



def save_to_file(data: list, name: str) -> None:
    """Сохранение вакансий в файл"""

    try:
        logger.info("Запущен скрипт сохранения в файл")
        today = datetime.datetime.today()
        today_str = today.strftime("%Y-%m-%d")
        file_path = f"data/{today_str}_{name.replace(" ", "_")}"

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            logger.info(f"Полученные данные сохранены в файл {file_path}")

    except Exception as ex:
        logger.error(f"Выполнение скрипта вызвало ошибку {ex}")