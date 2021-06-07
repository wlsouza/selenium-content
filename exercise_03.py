from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse

# Objective: Play and win the game

def find_anchor_by_attribute(browser, attribute, attr_value):
    elements = browser.find_elements_by_tag_name("a")
    for element in elements:
        if attr_value in str(element.get_attribute(attribute)):
            return element
            

def play_main_page(browser):
    ####### main page #######
    main = browser.find_element_by_tag_name("main")
    main.find_element_by_tag_name("a").click()
    sleep(2)

    play_first_page(browser)

def play_first_page(browser):
    ###### first page ######  
    ######## block that resolve the question #########
    # main = browser.find_element_by_tag_name("main")
    # problem = main.find_elements_by_tag_name("p")[1].text[0:-2]
    # sanitized_problem = problem.translate(str.maketrans("","",'+-*/ '))
    # if not sanitized_problem.isnumeric():
    #     browser.quit()
    #     raise ValueError("A expressão da pergunta contém caracteres inválidos.")
    # response = eval(problem)
    # anchors = main.find_elements_by_tag_name("a")
    # for anchor in anchors:
    #     if int(anchor.text) != response:
    #         anchor.click()
    #         break
    ###### easier way ######
    find_anchor_by_attribute(browser, "attr", "errado").click()
    sleep(20)
    play_second_page(browser)


def play_second_page(browser):
    ######## block that resolve the question #########
    # title = browser.title
    # elements = browser.find_elements_by_tag_name("a")
    # for element in elements:
    #     if element.text == title:
    #         element.click()
    #         break
    ###### easier way ######
    find_anchor_by_attribute(browser, "attr", "certo").click()
    sleep(4)
    play_third_page(browser)

def play_third_page(browser):
    ######## block that resolve the question #########
    # url = browser.current_url
    # path = urlparse(url).path.lstrip("/")
    # elements = browser.find_elements_by_tag_name("a")
    # for element in elements:
    #     if element.text == path:
    #         element.click()
    #         break
    ###### easier way ######
    find_anchor_by_attribute(browser, "href", "page_4.html").click()
    sleep(4)
    play_fourth_page(browser)

def play_fourth_page(browser):
    browser.refresh()


url = "https://selenium.dunossauro.live/exercicio_03.html"

browser = Firefox()
browser.get(url)
sleep(2)
play_main_page(browser)
browser.quit()