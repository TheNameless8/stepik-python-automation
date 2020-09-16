from selenium import webdriver

import time
import os
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/file_input.html')

input1 = browser.find_element_by_name("firstname")

input1.send_keys("Test")

input2 = browser.find_element_by_name("lastname")

input2.send_keys("Testerson")

input3 = browser.find_element_by_name("email")
input3.send_keys("test@te.st")


load = browser.find_element_by_id("file").send_keys(file_path)

browser.find_element_by_class_name("btn").click()


time.sleep(15)

browser.quit()
