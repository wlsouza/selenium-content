from selenium.webdriver import Firefox
from time import sleep

# Objective: Play and win the game of url

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

browser = Firefox()
browser.get(url)
sleep(2)

link = browser.find_element_by_tag_name("a")
expected_number = browser.find_elements_by_tag_name("p")[1].text[-1]


while True:
    link.click()
    result_number = browser.find_elements_by_tag_name("p")[-1].text[-1]
    win = result_number == expected_number
    print(f"Expected number = {expected_number}, result number = {result_number}, ganhou = {win}")
    if win:
        break

browser.quit()
