# Task_3 - Тестирование UI для Stellar Burgers

Автотесты для UI https://qa-stellarburgers.education-services.ru

## Описание проекта

Проект содержит тесты веб приложения Stella Burgers:

- Восстановление пароля
- Личный кабинет
- Проверка основного функционала
- Раздел "Лента заказов"

## Технологии

- **Python** 3.14.2
- **Pytest** 9.0.2
- **Allure** 2.38.1
- **Page Object Pattern**
- **Selenium** 4.41.0

#### Запуск всех тестов
pytest tests/ -v

#### Запуск конкретного теста
- pytest tests/test_login_page.py -v
- pytest tests/test_main_functionality.py -v
- pytest tests/test_order_page.py -v
- pytest tests/test_update_password.py -v

#### Открытие отчёта
allure open target/allure-report


 

 
 