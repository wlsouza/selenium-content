from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, unquote
from json import loads

# Objective: Fill and submit the form

def fill_form(browser, name, email, password, phone):
    browser.find_element_by_name("nome").send_keys(name)
    browser.find_element_by_name("email").send_keys(email)
    browser.find_element_by_name("senha").send_keys(password)
    browser.find_element_by_name("telefone").send_keys(phone)
    browser.find_element_by_name("btn").click()


url = "https://selenium.dunossauro.live/exercicio_04.html"

browser = Firefox()
browser.get(url)
sleep(2)

data = {
    "name": "Wellington",
    "email": "teste@teste.com.br",
    "password": "123456",
    "phone": "987654321",
}

fill_form(browser, **data)
sleep(1)
cur_url = browser.current_url
parsed_url = urlparse(unquote(cur_url))

info_list = parsed_url.query.split("&")
list_of_tuples = [tuple(info.split("=")) for info in info_list[:-1]]
url_info_dict = dict(list_of_tuples)

result_info_dict = loads(browser.find_element_by_tag_name("textarea").text.replace("\'", "\""))

browser.quit()

assert url_info_dict == result_info_dict

