"""Модуль для получения вакансий."""
from bs4 import BeautifulSoup
from selenium import webdriver


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


def get_vacations(link):
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
                "vacancy_description": vacation.find(
                    "div", class_="all-vacancies__table-main-title"
                ).get_text(strip=True),
                "vacancy_city": vacancy_city,
                "vacancy_date_publication": vacancy_date_publication,
                "vacancy_work_experience": vacancy_work_experience,
                "vacancy_employment": vacancy_employment,
                "vacancy_schedule": vacancy_schedule,
                "vacancy_salary": vacancy_salary,
            }
        )
    return vacancies


def young_professional_vacations():
    """Получение вакансий для молодых мпециалистов.

    Данная функция передаёт ссылку фунуции get_vacations(),
    для получения вакансий по направлению 'Молодым специалистам'
    """
    link = (
        "https://career.severstal.com/vacancies/?direction=%D0%BC%D0%B"
        "E%D0%BB%D0%BE%D0%B4%D0%BE%D0%B9+%D1%81%D0%BF%D0%B5%D1%86%D0"
        "%B8%D0%B0%D0%BB%D0%B8%D1%81%D1%82"
    )
    return get_vacations(link)


def manufacture_vacations():
    """Получение вакансий для работы на производстве.

    Данная функция передаёт ссылку фунуции get_vacations(),
    для получения вакансий по направлению 'Производство'
    """
    link = (
        "https://career.severstal.com/vacancies/?direction=%D0%BF%D1%8"
        "0%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE"
    )
    return get_vacations(link)


def it_and_digital_vacations():
    """Получение вакансий по направлению IT & Digital.

    Данная функция передаёт ссылку фунуции get_vacations(),
    для получения вакансий по направлению 'IT & Digital'
    """
    link = "https://career.severstal.com/vacancies/?direction=IT+%26+Digital"
    return get_vacations(link)


def office_vacations():
    """Получение вакансий для работы в офисе.

    Данная функция передаёт ссылку фунуции get_vacations(),
    для получения вакансий по направлению 'Офис'
    """
    link = (
        "https://career.severstal.com/vacancies/?direction=%D0%BE%D1%8"
        "4%D0%B8%D1%81"
    )
    return get_vacations(link)
