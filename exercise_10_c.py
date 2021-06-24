from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By

# Create a task and make it "walk" 4 times, always waiting (using the expected conditions) for the card to go to the next category before clicking the button.

def fill_task_form(browser, name, description):
    browser.find_element(By.ID, "todo-name").send_keys(name)
    browser.find_element(By.ID, "todo-desc").send_keys(description)
    browser.find_element(By.ID, "todo-submit").click()

def waits_the_card_to_be_in_category(waitwebdriver, category_id):
    locator = (By.CSS_SELECTOR, f"div#{category_id} div.terminal-card")
    waitwebdriver.until(
        presence_of_element_located(locator)
    )

def waits_the_card_to_be_in_category_and_click_on_button_do(webdriver, waitwebdriver, category_id):
    waits_the_card_to_be_in_category(waitwebdriver, category_id)
    # Click on the button
    webdriver.find_element(By.CSS_SELECTOR, "button.do").click()


url= "https://selenium.dunossauro.live/exercicio_10.html"

browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30)

# Generate task
fill_task_form(browser, "test", "testing")

# Waits the card appear in TODO category
waits_the_card_to_be_in_category_and_click_on_button_do(browser, wdw, "todo")

# Waits the card appear in DOING category
waits_the_card_to_be_in_category_and_click_on_button_do(browser, wdw, "doing")

# Waits the card appear in DONE category
waits_the_card_to_be_in_category_and_click_on_button_do(browser, wdw, "done")

# Waits the card appear in TODO category again
waits_the_card_to_be_in_category_and_click_on_button_do(browser, wdw, "todo")

# Waits the card appear in DOING category again before quit
waits_the_card_to_be_in_category(wdw, "doing")

browser.quit()


