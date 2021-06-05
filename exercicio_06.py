from selenium.webdriver import Firefox
from time import sleep
import re

def fill_form(browser, form_class, nome, senha):
    browser.find_element_by_css_selector(f'form.{form_class} input[name="nome"]').send_keys(nome)
    browser.find_element_by_css_selector(f'form.{form_class} input[name="senha"]').send_keys(senha)
    browser.find_element_by_css_selector(f'form.{form_class} input[type="submit"]').click()
    

url = "https://selenium.dunossauro.live/exercicio_06.html"

browser = Firefox()
browser.get(url)

first_text = browser.find_element_by_css_selector('header>p:first-child').text
number_of_times = int(re.findall("[0-9]+", first_text)[0])

for _ in range(number_of_times):
    sleep(2)
    target_form = browser.find_element_by_css_selector('header span:not(#num)').text
    fill_form(browser, "form-"+target_form, f"Wellington{_}", "123456")

browser.quit()