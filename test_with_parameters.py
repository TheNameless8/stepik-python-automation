import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Функция, выполняющая расчет передаваемого ответа
def calc():
    answer = str(math.log(int(time.time())))
    return answer

# Фикстура запуска и закрытия окна браузера для каждого теста
@pytest.fixture(scope="function")
def browser():
    print("\n___start browser for test..__")
    browser = webdriver.Chrome()
    yield browser
    print("\n___quit browser..____")
    browser.quit()

# Парраметризованная тестовая функция
@pytest.mark.parametrize('page', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_alien_message(browser, page):
    # Открытие страницы браузера
    link = f'https://stepik.org/lesson/{page}/step/1'
    browser.get(link)

    # Ожидание загрузки поля ввода ответа
    textarea = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
    )
    # Ввод ответа
    textarea.send_keys(calc())

    # Ожидание кликабельности кнопки отправки ответа, клик по ней
    button  = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))

    )
    button.click()

    # Ожидание появления дополнительного сообщения

    message = WebDriverWait(browser,10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
    )
    # Проверка, что текст в опциональном фидбеке совпадает с "Correct!"
    assert message.text == "Correct!", f'Wrong text! Should Be "Correct!", actual "{message.text}"'
