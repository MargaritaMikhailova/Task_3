import random
import string

from selenium.webdriver.common.by import By

from data import Domain


def random_string(length: int = 10) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


def random_string_email(length: int = 10) -> str:
    local_part = random_string(length)
    return f"{local_part}@{Domain.DOMAIN}"


def extract_order_number(text: str) -> str | None:
    text = text.strip()
    if "#" in text:
        number = text.split("#", 1)[1].split()[0]
        return number.lstrip("0") or number
    if text.isdigit():
        return text.lstrip("0") or text
    return None


def ingredient_by_name(name: str):
    return (By.XPATH, f"//p[contains(text(), '{name}')]/parent::a")


def counter_by_ingredient(name: str):
    return (By.XPATH, f"//p[contains(text(), '{name}')]/parent::a//div[contains(@class, 'counter')]")
