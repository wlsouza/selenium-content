from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from functools import partial

# Objective: Find the class selenium in the button that change randomly

def waits_until_the_element_has_the_class(selector, class_name, webdriver):
    try:
        element = webdriver.find_element_by_css_selector(selector)
        if element:
            if class_name in element.get_attribute("class"):
                return True
            return False
        return False
    except StaleElementReferenceException:
        return False

url = "https://selenium.dunossauro.live/exercicio_09.html"

browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30, poll_frequency=0.4)

button_has_selenium_class = partial(waits_until_the_element_has_the_class, "button", "selenium")

wdw.until(button_has_selenium_class, message="the class selenium can not founded")
print("botão encontrado")
browser.quit()
