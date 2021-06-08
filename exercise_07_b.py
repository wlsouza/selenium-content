from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from time import sleep

# Objective: Play the game and get the values of label before and after it change.

class EventListener(AbstractEventListener):
    def before_click(self, element, driver):
        if element.tag_name == "a":
            print(f"O valor da resposta escolhida é: \"{element.text}\"")
        # return super().after_click(element, driver)

    def after_navigate_to(self, url, driver):
        print(f"O endereço da próxima página é: \"{url}\"")
        # return super().after_navigate_to(url, driver)

def play_main_page(browser):
    ####### main page #######
    print("========== MAIN PAGE ==========")
    # main = browser.find_element_by_tag_name("main")
    # main.find_element_by_tag_name("a").click()
    browser.find_element_by_css_selector("main a").click()
    print("===============================")
    sleep(2)
    play_first_page(browser)

def play_first_page(browser):
    print("========== FIRST PAGE ==========")
    browser.find_element_by_css_selector("a[attr=errado]").click()
    print("================================")
    sleep(20)
    play_second_page(browser)


def play_second_page(browser):
    print("========== SECOND PAGE ==========")
    browser.find_element_by_css_selector("a[attr=certo]").click()
    print("=================================")
    sleep(4)
    play_third_page(browser)

def play_third_page(browser):
    print("========== THIRD PAGE ==========")
    browser.find_element_by_css_selector("a[href='page_4.html']").click()
    print("================================")
    sleep(4)
    play_fourth_page(browser)

def play_fourth_page(browser):
    print("========== FOURTH PAGE ==========")
    browser.refresh()
    print("=================================")

url = "https://selenium.dunossauro.live/exercicio_03.html"

browser = Firefox()
browser = EventFiringWebDriver(browser, EventListener())
browser.get(url)
sleep(2)
play_main_page(browser)
browser.quit()