install: # установка poetry
	poetry install

brain-games: # запуск на выполнение файла brain_games.py
	poetry run brain-games

build: # сборка пакета с помощью poetry
	poetry build

publish: # отладка публикации без добавления в PyPI
	poetry publish --dry-run

package-install: # установка пакета из операционной системы
	python3 -m pip install --user dist/*.whl

# activate: #запуск вируального окружения
#	source ./.venv/bin/activate

lint: #запуск линтера
	poetry run flake8 brain_games
