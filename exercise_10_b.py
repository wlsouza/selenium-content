from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, text_to_be_present_in_element
from selenium.webdriver.common.by import By

# Objective: Play the game using expected conditions (waits).

def wait_and_click(browser, webdriverwait, locator):
    webdriverwait.until(
        presence_of_element_located(locator)
    )
    browser.find_element(*locator).click()


url = "https://selenium.dunossauro.live/exercicio_03.html"

browser = Firefox()
wdw = WebDriverWait(browser, 30)

browser.get(url)

locator_main_page = (By.CSS_SELECTOR, "main a")
locator_first_page = (By.CSS_SELECTOR, "a[attr=errado]")
locator_second_page = (By.CSS_SELECTOR, "a[attr=certo]")
locator_third_page = (By.CSS_SELECTOR, "a[href='page_4.html']")
locator_fourth_page = (By.CSS_SELECTOR, "main p")

wait_and_click(browser, wdw, locator_main_page)
wait_and_click(browser, wdw, locator_first_page)
wait_and_click(browser, wdw, locator_second_page)
wait_and_click(browser, wdw, locator_third_page)

wdw.until(
    text_to_be_present_in_element(locator_fourth_page, "refresh")
)
browser.refresh()

browser.quit()