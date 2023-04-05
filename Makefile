MANAGE := poetry run python3 web/scraper/manage.py

shell:
	poetry run scrapy shell
django-shell:
	${MANAGE} shell_plus --plain
start:
	${MANAGE} runserver 127.0.0.1:8000
migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate