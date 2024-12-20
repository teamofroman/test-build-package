import os
from pathlib import Path

from dotenv import load_dotenv
from setuptools import find_packages, setup

from generator import generate


def read_dependencies() -> list[str]:
    """Автоматически находит файл с зависимостями.

    Поддерживаемые форматы:
    - src/requirements.txt: Стандартный текстовый файл с зависимостями.

    :return: Список зависимостей в формате ['package==version', ...].
    :raises FileNotFoundError: Если ни один из файлов не найден.
    """
    requirements_file = Path("package/requirements.txt")

    if requirements_file.exists():
        return requirements_file.read_text().splitlines()

    raise FileNotFoundError(
        "Файл с зависимостями не обнаружен. "
        "Поддерживаемые форматы: requirements.txt",
    )


load_dotenv()

if __name__ == "__main__":
    generate()
    setup(
        name="test_package_test_demo",
        version=os.getenv("PACKAGE_VERSION", "0.0.1"),
        author="Author",
        author_email="author@yandex.ru",
        description="Тестовый пакет",
        long_description=Path("package/README.md").read_text(),
        long_description_content_type="text/markdown",
        package_dir={"": "package"},
        packages=find_packages(where="package"),
        python_requires=">=3.11",
        install_requires=read_dependencies(),
        classifiers=[
            "Programming Language :: Python :: 3.11",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Development Status :: 2 - Pre-Alpha",
        ],
    )
