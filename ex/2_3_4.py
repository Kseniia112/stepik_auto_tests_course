from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем кнопку
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

    # подтверждаем
    confirm = browser.switch_to.alert
    confirm.accept()

    # считываем x
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)

    # записываем результат
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    # Нажимаем кнопку
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()