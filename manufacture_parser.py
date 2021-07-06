import requests
from bs4 import BeautifulSoup
import json


URL = 'https://career.severstal.com/vacancies/?direction=%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE'
HEADERS = {
	'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
	'accept' : '*/*'
}
FILE = ['manufacture_belgorod.txt', 
	'manufacture_voroneg.txt',
	'manufacture_moscow.txt',
	'manufacture_eagle.txt',
	'manufacture_yaroslavl.txt',
	'manufacture_vorkuta.txt',
	'manufacture_kolpino.txt',
	'manufacture_olenegorsk.txt',
	'manufacture_saint_petersburg.txt',
	'manufacture_cherepovets.txt',
	'manufacture_novosibirsk.txt',
	'manufacture_kazan.txt',
	]


def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def parse_manufacture(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('a', class_='all-vacancies__table-tr js-all-vacancies-item')
	about_profession = []
	for item in items:
		ss = item.find_all('div', class_='all-vacancies__table-td-content col-xs-12 col-sm-24')
		information_about_work = []
		for s in ss:
			information_about_work.append(s.get_text(strip=True))
		if information_about_work[4] == '':
			information_about_work[4] = 'Не указано'
		about_profession.append([item.find('div', class_='all-vacancies__table-main-title').get_text(strip=True),
			item.find('div', class_='all-vacancies__table-main-sub-title').get_text(strip=True),
			information_about_work[0],
			information_about_work[1],
			information_about_work[2],
			information_about_work[3],
			information_about_work[4]
			])
	return about_profession


def save_file(items, path):
	for item in items:
		if 'Белгород' in item:
			with open(path[0], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Воронеж' in item:
			with open(path[1], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Москва' in item:
			with open(path[2], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Орёл' in item:
			with open(path[3], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Ярославль' in item:
			with open(path[4], 'a+', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Воркута' in item:
			with open(path[5], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Колпино' in item:
			with open(path[6], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Оленегорск' in item:
			with open(path[7], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Санкт-Петербург' in item:
			with open(path[8], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Череповец' in item:
			with open(path[9], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Новосибирск' in item:
			with open(path[10], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')
		elif 'Казань' in item:
			with open(path[11], 'a', encoding='utf-8') as file:
				file.write(', '.join(item) + '\n')



def parse():
	html = get_html(URL)
	if html.status_code == 200:
		infa = []
		infa.extend(parse_manufacture(html.text))
		save_file(infa, FILE)
	else:
		print('Error')


parse()






