"""Модуль для получения вакансий с сайта Северстали."""
from dataclasses import dataclass

from bs4 import BeautifulSoup
from selenium import webdriver


URL_PATTERN = "https://career.severstal.com/vacancies/?direction={direction}"
VACANCIES_DIRECTIONS = {
    "Производство": "производство",
    "IT & Digital": "IT+%26+Digital",
    "Офис": "офис",
    "Молодым специалистам": "молодой+специалист",
}
ALLOWED_VACANCY_CITIES = {
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
}


@dataclass
class Vacancy:
    """Модель вакансии с сайта Северстали."""

    direction: str
    description: str
    city: str
    date_publication: str
    work_experience: str
    employment: str
    schedule: str
    salary: str


def get_vacancies():
    """Получение вакансий всех направлений."""
    vacancies = []
    for direction in VACANCIES_DIRECTIONS:
        direction_vacancies = _get_direction_vacancies(direction)
        vacancies.extend(direction_vacancies)

    return vacancies


def _get_direction_vacancies(vacancy_direction):
    """Получение вакансий конкретного направления."""
    url = URL_PATTERN.format(direction=VACANCIES_DIRECTIONS[vacancy_direction])
    page_content = _get_page_content(url)
    vacancies_page_elements = _get_vacancies_page_elements(page_content)

    vacancies = []
    for vacancy_page_element in vacancies_page_elements:
        vacancy = _get_vacancy_from_page_element(
            vacancy_page_element, vacancy_direction
        )
        if vacancy.city not in ALLOWED_VACANCY_CITIES:
            continue

        if not vacancy.salary:
            vacancy.salary = "Не указано"

        vacancies.append(vacancy)

    return vacancies


def _get_page_content(url):
    """Получение html-контента страницы по переданной ссылке."""
    with webdriver.Chrome() as driver:
        driver.get(url)
        return driver.page_source


def _get_vacancies_page_elements(page_content):
    """Получение элементов вакансий со страницы сайта."""
    soup = BeautifulSoup(page_content, "lxml")
    vacancies_page_elements = soup.find_all(
        "a", class_="all-vacancies__table-tr"
    )
    return vacancies_page_elements


def _get_vacancy_from_page_element(page_element, vacancy_direction):
    """Получение вакансии из элемента вакансии со страницы."""
    vacancy_description = page_element.find(
        "div", class_="all-vacancies__table-main-title"
    ).get_text(strip=True)
    vacancy_city = page_element.find(
        "div", class_="all-vacancies__table-main-sub-title"
    ).get_text(strip=True)
    vacancy_element_fields = page_element.find_all(
        "div",
        class_="all-vacancies__table-td-content",
    )
    (
        vacancy_date_publication,
        vacancy_work_experience,
        vacancy_employment,
        vacancy_schedule,
        vacancy_salary,
    ) = (
        vacancy_element_field.get_text(strip=True)
        for vacancy_element_field in vacancy_element_fields
    )

    return Vacancy(
        direction=vacancy_direction,
        description=vacancy_description,
        city=vacancy_city,
        date_publication=vacancy_date_publication,
        work_experience=vacancy_work_experience,
        employment=vacancy_employment,
        schedule=vacancy_schedule,
        salary=vacancy_salary,
    )
