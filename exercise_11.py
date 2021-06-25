from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By

# fill and submit the form using ready-made waits (expected_conditions)

def wait_element(waitwebdriver, locator):
    waitwebdriver.until(
        element_to_be_clickable(locator)
    )

def wait_and_fill_element(webdriver, waitwebdriver, locator, content_to_fill):
    wait_element(waitwebdriver, locator)
    webdriver.find_element(*locator).send_keys(content_to_fill)


url= "https://selenium.dunossauro.live/exercicio_11.html"

browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30)

# fill the form
wait_and_fill_element(browser, wdw, (By.NAME, "nome"), "Wellington")
wait_and_fill_element(browser, wdw, (By.NAME, "email"), "test@test.com.br")
wait_and_fill_element(browser, wdw, (By.NAME, "c_email"), "test@test.com.br")
wait_and_fill_element(browser, wdw, (By.NAME, "senha"), "123456")
wait_and_fill_element(browser, wdw, (By.NAME, "c_senha"), "123456")

# submit
button_locator = (By.NAME, "button")
wait_element(wdw, button_locator)
browser.find_element(*button_locator).click()

browser.quit()