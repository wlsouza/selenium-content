from selenium.webdriver import Firefox
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from time import sleep

# Objective: Fill in the form and get the values of label before and after it change.

class EventListener(AbstractEventListener):

    def before_change_value_of(self, element, driver):
        if element.tag_name == "input":
            label = browser.find_element_by_css_selector(f"label[for={element.get_attribute('id')}]")
            print(f"O valor antes do <span> ser alterado é: \"{label.text}\"")
        # return super().before_change_value_of(element, driver)

    def after_change_value_of(self, element, driver):
        if element.tag_name == "input":
            label = browser.find_element_by_css_selector(f"label[for={element.get_attribute('id')}]") 
            print(f"O valor depois do <span> ser alterado é: \"{label.text}\"")
        # return super().after_change_value_of(element, driver)

url = "https://selenium.dunossauro.live/exercicio_07.html"

browser = Firefox()
browser = EventFiringWebDriver(browser, EventListener())

browser.get(url)
sleep(1)

print("========== NAME ==========")
name_input = browser.find_element_by_css_selector('input#nome').send_keys("Wellington")
print("==========================")
print("========== EMAIL ==========")
email_input = browser.find_element_by_css_selector("input#email").send_keys("teste@teste")
print("===========================")
print("========== SENHA ==========")
email_input = browser.find_element_by_css_selector("input#senha").send_keys("1234")
print("===========================")

browser.quit()