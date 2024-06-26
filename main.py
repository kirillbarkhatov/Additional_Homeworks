from src.vacancy import get_vacancies
from src.save_to_file import save_to_file
import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"logs/logs.log", mode="a")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


if __name__ == "__main__":
    logger.info("Программа запущена")

    query = input("Введите запрос на поиск вакансий: ")
    logger.info(f"Пользователь ввел запрос {query}")
    exclude_words = input("Введите слова-исключения из поиска (через пробел): ").split()
    logger.info(f"Пользователь ввел список слов исключений {exclude_words}")

    logger.info("Обращение к функции получения данных")
    data = get_vacancies(query, exclude_words)

    logger.info("Обращение к функции сохранения в файл")
    save_to_file(data, query)

    logger.info("Программа завершена")
