from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
import math, time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

browser.find_element_by_id("book").click()


x = int(browser.find_element_by_id("input_value").text)

res = str(math.log(abs(12*math.sin(x))))

browser.find_element_by_id("answer").send_keys(res)

browser.find_element_by_id('solve').click()

time.sleep(15)

browser.quit()
