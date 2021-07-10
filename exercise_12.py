from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, alert_is_present
from selenium.webdriver.common.by import By

# objective: fill and submit the form and validate the result.

def wait_element(webdriverwait, locator):
    webdriverwait.until(
        element_to_be_clickable(locator)
    )

def wait_alert(webdriverwait):
    webdriverwait.until(
        alert_is_present()
    )


def wait_and_fill_element(webdriver, webdriverwait, locator, content_to_fill):
    wait_element(webdriverwait, locator)
    webdriver.find_element(*locator).click()
    wait_alert(webdriverwait)
    prompt = webdriver.switch_to.alert
    prompt.send_keys(content_to_fill)
    prompt.accept()


url= "https://selenium.dunossauro.live/exercicio_12.html"

browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30)


form_data = {
    "name": "Wellington",
    "email": "test@test.com.br",
    "sign": "aries"
}

# fill the form
wait_and_fill_element(browser, wdw, (By.NAME, "nome"), form_data.get("name"))
wait_and_fill_element(browser, wdw, (By.NAME, "email"), form_data.get("email"))
wait_and_fill_element(browser, wdw, (By.NAME, "signo"), form_data.get("sign"))

# submit
button_locator = (By.CSS_SELECTOR, "input[type=submit]")
wait_element(wdw, button_locator)
browser.find_element(*button_locator).click()

# validate 
browser.switch_to.window(browser.window_handles[-1])
wait_element(wdw, (By.CSS_SELECTOR, "div h1"))
elements = browser.find_elements(By.CSS_SELECTOR, "div h1")
print(f"Elements of result popup: {', '.join([element.text for element in elements])}.")
for value in form_data.values():
    for element in elements:
        if value in element.text:
            print(f"Value \"{value}\" founded.")
            break
    else:
        raise ValueError(f"Value \"{value}\" not founded in the result popup.")

browser.quit()