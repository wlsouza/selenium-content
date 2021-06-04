from selenium.webdriver import Firefox
from time import sleep

def fill_form(browser, form_class, nome, senha):
    browser.find_element_by_css_selector(f'form.{form_class} input[name="nome"]').send_keys(nome)
    browser.find_element_by_css_selector(f'form.{form_class} input[name="senha"]').send_keys(senha)
    browser.find_element_by_css_selector(f'form.{form_class} input[type="submit"]').click()
    

url = "https://selenium.dunossauro.live/exercicio_05.html"

browser = Firefox()
browser.get(url)

while True:
    sleep(1)
    target_form = browser.find_element_by_css_selector('header span').text
    if target_form == "... Mentira, você conseguiu terminar":
        break
    fill_form(browser, "form-"+target_form, "Wellington", "123456")

browser.quit()