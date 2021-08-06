"""Модуль для получения вакансий."""
from dataclasses import dataclass

from bs4 import BeautifulSoup
from selenium import webdriver


URL_PATTERN = "https://career.severstal.com/vacancies/?direction={direction}"
DIRECTIONS_LINK = {
    "производство": "Производство",
    "IT+%26+Digital": "IT & Digital",
    "офис": "Офис",
    "молодой+специалист": "Молодым специалистам",
}
CITIES = [
    "Череповец",
    "Ярославль",
    "Москва",
    "Белгород",
    "Воронеж",
    "Орел",
    "Воркута",
    "Колпино",
    "Оленегорск",
    "Санкт-Петербург",
    "Новосибирск",
    "Казань",
]


@dataclass
class Vacancy:
    """Класс для упорядочивания информации о вакансиях."""

    vacancy_direction: str
    vacancy_description: str
    vacancy_city: str
    vacancy_date_publication: str
    vacancy_work_experience: str
    vacancy_employment: str
    vacancy_schedule: str
    vacancy_salary: str


def get_content(link, vacancy_direction):
    """Получение вакансий по переданной ссылке.

    Эта функция запрашивает код у страницы по переданной ссылке,
    обрабатывает её,
    на выходе выдаёт список словарей с вакансиями.
    """
    driver = webdriver.Chrome()
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()
    vacancies = []
    vacations = soup.find_all("a", class_="all-vacancies__table-tr")
    for vacation in vacations:
        vacancy_description = vacation.find(
            "div", class_="all-vacancies__table-main-title"
        ).get_text(strip=True)
        vacancy_city = vacation.find(
            "div", class_="all-vacancies__table-main-sub-title"
        ).get_text(strip=True)
        vacancy_information = vacation.find_all(
            "div",
            class_="all-vacancies__table-td-content",
        )
        (
            vacancy_date_publication,
            vacancy_work_experience,
            vacancy_employment,
            vacancy_schedule,
            vacancy_salary,
        ) = (i.get_text(strip=True) for i in vacancy_information)
        if vacancy_city not in CITIES:
            continue
        if vacancy_salary == "":
            vacancy_salary = "Не указано"
        vacancies.append(
            Vacancy(
                vacancy_direction=vacancy_direction,
                vacancy_description=vacancy_description,
                vacancy_city=vacancy_city,
                vacancy_date_publication=vacancy_date_publication,
                vacancy_work_experience=vacancy_work_experience,
                vacancy_employment=vacancy_employment,
                vacancy_schedule=vacancy_schedule,
                vacancy_salary=vacancy_salary,
            )
        )

    return vacancies


def get_vacancies():
    """Функция для получения вакансий по всем направлениям.

    Данная функция через цикл передаёт ссылки функции get_content()
    и возвращает словарь со списками вакансий,
    где ключами являются названия направлений.
    """
    vacancies = []
    for direction in DIRECTIONS_LINK.keys():
        direction_vacancies = get_content(
            URL_PATTERN.format(direction=direction), DIRECTIONS_LINK[direction]
        )
        vacancies.extend(direction_vacancies)

    return vacancies
