"""Модуль для получения вакансий с сайта Северстали."""
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
    """Модель вакансии с сайта Северстали."""

    vacancy_direction: str
    vacancy_description: str
    vacancy_city: str
    vacancy_date_publication: str
    vacancy_work_experience: str
    vacancy_employment: str
    vacancy_schedule: str
    vacancy_salary: str


def get_content(link, vacancy_direction):
    """Получение вакансий конкретного направления по переданной ссылке."""
    page_content = _get_page_content(link)
    vacancies_page_elements = _get_vacancies_page_elements(page_content)
    vacancies = []
    for vacancy_page_element in vacancies_page_elements:
        vacancy = _get_vacancy_from_page_element(
            vacancy_page_element, vacancy_direction
        )
        if vacancy.city not in CITIES:
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
    vacancy_information = page_element.find_all(
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

    return Vacancy(
        vacancy_direction=vacancy_direction,
        vacancy_description=vacancy_description,
        vacancy_city=vacancy_city,
        vacancy_date_publication=vacancy_date_publication,
        vacancy_work_experience=vacancy_work_experience,
        vacancy_employment=vacancy_employment,
        vacancy_schedule=vacancy_schedule,
        vacancy_salary=vacancy_salary,
    )


def get_vacancies():
    """Получение вакансий всех направлений."""
    vacancies = []
    for direction in DIRECTIONS_LINK.keys():
        direction_vacancies = get_content(
            URL_PATTERN.format(direction=direction), DIRECTIONS_LINK[direction]
        )
        vacancies.extend(direction_vacancies)

    return vacancies
