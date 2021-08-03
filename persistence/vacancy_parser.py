"""Модуль для получения вакансий."""
from bs4 import BeautifulSoup
from selenium import webdriver


LINK = "https://career.severstal.com/vacancies/?direction="
DIRECTIONS_LINK = [
    "производство",
    "IT+%26+Digital",
    "офис",
    "молодой+специалист",
]
DIRECTIONS = [
    "Производство",
    "IT & Digital",
    "Офис",
    "Молодым специалистам",
]
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


def get_content(link):
    """Получение вакансий по переданной ссылке.

    Эта функция запрашивает код у страницы по переданной ссылке,
    обрабатывает её,
    на выходе выдаёт список словарей с вакансиями.
    """
    driver = webdriver.Chrome()
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()
    vacations = soup.find_all("a", class_="all-vacancies__table-tr")
    vacancies = []
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
            {
                "vacancy_description": vacancy_description,
                "vacancy_city": vacancy_city,
                "vacancy_date_publication": vacancy_date_publication,
                "vacancy_work_experience": vacancy_work_experience,
                "vacancy_employment": vacancy_employment,
                "vacancy_schedule": vacancy_schedule,
                "vacancy_salary": vacancy_salary,
            }
        )
    return vacancies


def get_vacancies():
    """Функция для получения вакансий по всем направлениям.

    Данная функция через цикл передаёт ссылки функции get_content()
    и возвращает словарь со списками вакансий,
    где ключами являются названия направлений.
    """
    vacancies = {}
    for i in range(len(DIRECTIONS_LINK)):
        vacancies[DIRECTIONS[i]] = get_content(LINK + DIRECTIONS_LINK[i])
    return vacancies
