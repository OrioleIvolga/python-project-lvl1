install: # установка poetry
        poetry install

brain-games: # пока не знаю зачем, потом допишу
        poetry run brain-games
        
build: # сборка пакета с помощью poetry
        poetry build
        
publish: # отладка публикации без добавления в PyPI
        poetry publish --dry-run
        
package-install: # установка пакета из операционной системы
        python3 -m pip install --user dist/*.whl
