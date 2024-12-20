# Проверка активации окружения
ifeq ($(VIRTUAL_ENV),)
    $(error 'Виртуальное окружение не активировано! Активируйте его перед запуском команд Make.')
endif

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Определение необходимых путей для запуска команд
PYTHON := "$(VIRTUAL_ENV)/bin/python"
TWINE := "$(VIRTUAL_ENV)/bin/twine"

# Меню команд
.PHONY: help
help:
	@echo "Доступные команды:"
	@echo "  help          Показывает список всех команд"
	@echo "  build         Собирает проект в дистрибутив"
	@echo "  clean         Удаляет временные файлы и кеш"

# Сборка приложения в дистрибутив
.PHONY: build
build:
	$(PYTHON) setup.py sdist bdist_wheel

# Очистка кеша и временных файлов
.PHONY: clean
clean:
	rm -rf build/ dist/ __pycache__ *.egg-info
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	find . -name '*.egg-info' -type d -exec rm -rf {} +


# Сборка и публикация пакета на TestPyPI
.PHONY: upload
upload: clean build
	@echo "Публикация пакета на TestPyPI."
	TWINE_USERNAME=$(TWINE_USERNAME) TWINE_PASSWORD=$(TWINE_PASSWORD) $(TWINE) upload -r testpypi dist/*