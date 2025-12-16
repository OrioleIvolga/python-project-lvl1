install: # установка poetry
	poetry install

brain-games: # запуск на выполнение файла brain_games.py
	poetry run brain-games

brain-even: # запуск на выполнение файла brain_even.py
	poetry run brain-even

brain-calc: # запуск на выполнение файла brain_calc.py
	poetry run brain-calc

brain-gcd: # запуск на выполнение файла brain_gsd.py
	poetry run brain-gcd

brain-progr: # запуск на выполнение файла brain_progression.py
	poetry run brain-progression

brain-prime: # запуск на выполнение файла brain_prime.py
	poetry run brain-prime

build: # сборка пакета с помощью poetry
	poetry build

publish: # отладка публикации без добавления в PyPI
	poetry publish --dry-run

package-install: # установка пакета из операционной системы
	python3 -m pip install --user dist/*.whl

lint: #запуск линтера
	poetry run flake8 brain_games/
