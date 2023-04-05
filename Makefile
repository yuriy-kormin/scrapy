MANAGE := poetry run python3 web/scraper/manage.py

shell:
	poetry run scrapy shell
django-shell:
	${MANAGE} shell_plus --plain