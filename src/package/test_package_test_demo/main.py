import requests


def get_url(url: str) -> tuple[int, str]:
    if not url:
        return (-1, "")

    response = requests.get(url)

    return response.status_code, response.text


def hello() -> None:
    print("Hello, world!")
