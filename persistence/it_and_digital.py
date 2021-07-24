from selenium import webdriver


FILE = ['it_and_digital_belgorod.txt', 
	'it_and_digital_voroneg.txt',
	'it_and_digital_moscow.txt',
	'it_and_digital_eagle.txt',
	'it_and_digitalyaroslavl.txt',
	'it_and_digital_vorkuta.txt',
	'it_and_digital_kolpino.txt',
	'it_and_digital_olenegorsk.txt',
	'it_and_digital_saint_petersburg.txt',
	'it_and_digital_cherepovets.txt',
	'it_and_digital_novosibirsk.txt',
	'it_and_digital_kazan.txt'
	]

driver = webdriver.Chrome()
driver.get('https://career.severstal.com/vacancies/?direction=IT+%26+Digital')
vacations = driver.find_elements_by_class_name('all-vacancies__table-tbody')
vacations_in_belgorod = []
vacations_in_voroneg = []
vacations_in_moscow = []
vacations_in_eagle = []
vacations_in_yaroslavl = []
vacations_in_vorkuta = []
vacations_in_kolpino = []
vacations_in_olenegorsk = []
vacations_in_saint_petersburg = []
vacations_in_cherepovets = []
vacations_in_novosibirsk = []
vacations_in_kazan = []
list1 = []
items = []
for vacation in vacations:
	list1.append(vacation.text)
per = sum([lis.split('\n') for lis in list1], [])
driver.quit()
while per != []:
	for p in per:
		if len(per) < 7:
			items.append(', '.join(per[:6]) + ', Не указано')
			del per[:6]
			break			
		else:
			if '₽' in per[6]:
				items.append(', '.join(per[:7]))
				del per[:7]
				break
			else:
				items.append(', '.join(per[:6]) + ', Не указано')
				del per[:6]
				break

for item in items:
	if 'Белгород' in item:
		vacations_in_belgorod.append(item)
	elif 'Воронеж' in item:
		vacations_in_voroneg.append(item)
	elif 'Москва' in item:
		vacations_in_moscow.append(item)
	elif 'Орёл' in item:
		vacations_in_eagle.append(item)
	elif 'Ярославль' in item:
		vacations_in_yaroslavl.append(item)
	elif 'Воркута' in item:
		vacations_in_vorkuta.append(item)
	elif 'Колпино' in item:
		vacations_in_kolpino.append(item)
	elif 'Оленегорск' in item:
		vacations_in_olenegorsk.append(item)
	elif 'Санкт-Петербург' in item:
		vacations_in_saint_petersburg.append(item)
	elif 'Череповец' in item:
		vacations_in_cherepovets.append(item)
	elif 'Новосибирск' in item:
		vacations_in_novosibirsk.append(item)
	elif 'Казань' in item:
		vacations_in_kazan.append(item)

	
def save_file(path):
	with open(path[0], 'w', encoding='utf-8') as file:
		if vacations_in_belgorod == []:
			file.write('К сожалению в Белгороде сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_belgorod:
				file.write(vacation + '\n')


	with open(path[1], 'w', encoding='utf-8') as file:
		if vacations_in_voroneg == []:
			file.write('К сожалению в Воронеже сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_voroneg:
				file.write(vacation + '\n')


	with open(path[2], 'w', encoding='utf-8') as file:
		if vacations_in_moscow == []:
			file.write('К сожалению в Москве сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_moscow:
				file.write(vacation + '\n')


	with open(path[3], 'w', encoding='utf-8') as file:
		if vacations_in_eagle == []:
			file.write('К сожалению в Орле сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_eagle:
				file.write(vacation + '\n')


	with open(path[4], 'w', encoding='utf-8') as file:
		if vacations_in_yaroslavl == []:
			file.write('К сожалению в Ярославле сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_yaroslavl:
				file.write(vacation + '\n')


	with open(path[5], 'w', encoding='utf-8') as file:
		if vacations_in_vorkuta == []:
			file.write('К сожалению в Воркуте сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_vorkuta:
				file.write(vacation + '\n')


	with open(path[6], 'w', encoding='utf-8') as file:
		if vacations_in_kolpino == []:
			file.write('К сожалению в Колпино сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_kolpino:
				file.write(vacation + '\n')


	with open(path[7], 'w', encoding='utf-8') as file:
		if vacations_in_olenegorsk == []:
			file.write('К сожалению в Оленегорске сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_olenegorsk:
				file.write(vacation + '\n')


	with open(path[8], 'w', encoding='utf-8') as file:
		if vacations_in_saint_petersburg == []:
			file.write('К сожалению в Санкт-Петербурге сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_saint_petersburg:
				file.write(vacation + '\n')


	with open(path[9], 'w', encoding='utf-8') as file:
		if vacations_in_cherepovets == []:
			file.write('К сожалению в Череповце сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_cherepovets:
				file.write(vacation + '\n')


	with open(path[10], 'w', encoding='utf-8') as file:
		if vacations_in_novosibirsk == []:
			file.write('К сожалению в Новосибирске сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_novosibirsk:
				file.write(vacation + '\n')


	with open(path[11], 'w', encoding='utf-8') as file:
		if vacations_in_kazan == []:
			file.write('К сожалению в Казани сейчас нет работы в IT и DIGITAL' + '\n')
		else:
			for vacation in vacations_in_kazan:
				file.write(vacation + '\n')

save_file(FILE)