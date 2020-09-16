from selenium import webdriver
import time, math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

browser.find_element_by_class_name("btn").click()

new_window = browser.window_handles[1]

browser.switch_to.window(new_window)

x = int(browser.find_element_by_id("input_value").text)

res = str(math.log(abs(12*math.sin(x))))

browser.find_element_by_id("answer").send_keys(res)

browser.find_element_by_class_name('btn').click()


time.sleep(20)
browser.quit()
