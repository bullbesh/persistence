import sqlite3
from manufacture_parser import get_manufacture_vacations
from it_and_digital import get_it_and_digital_vacations
from office import get_office_vacations
from young_professional import get_young_professional_vacation
import asyncio


def init_db(force):
	db = sqlite3.connect('vacations.db')
	cursor = db.cursor()
	if force:
		cursor.execute("DROP TABLE IF EXISTS vacations")

	cursor.execute("""CREATE TABLE IF NOT EXISTS vacations (
		direction TEXT,
		description TEXT,
		city TEXT,
		published TEXT,
		schedule TEXT,
		hours TEXT,
		salary TEXT
	)""")



	db.commit()
	for item in get_manufacture_vacations():
		cursor.execute("INSERT INTO vacations (direction, description, city, published, schedule, hours, salary")

if __name__ == '__main__':
	init_db(True)
