from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from functools import partial

# Create a task and make it "walk" 4 times, always waiting (using self-made waits) for the card to go to the next category before clicking the button.

def fill_task_form(browser, name, description):
    browser.find_element_by_id("todo-name").send_keys(name)
    browser.find_element_by_id("todo-desc").send_keys(description)
    browser.find_element_by_id("todo-submit").click()

def waits_the_card_to_be_inside_specific_div(div_id, webdriver):
    card = webdriver.find_element_by_css_selector(f"div#{div_id} div.terminal-card")
    if card:
        return True
    return False

def waits_the_card_to_be_in_category(waitwebdriver, category_id):
    waits_the_card_in_div = partial(waits_the_card_to_be_inside_specific_div, category_id)
    waitwebdriver.until(waits_the_card_in_div)


def waits_the_card_to_be_in_category_and_click_on_button_do(webdriver, waitwebdriver, category_id):
    waits_the_card_to_be_in_category(waitwebdriver, category_id)
    # Click on the button
    webdriver.find_element_by_css_selector("button.do").click()


url= "https://selenium.dunossauro.live/exercicio_10.html"

browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30)

# Generate task
fill_task_form(browser, "test", "testing")

# Waits card appear in TODO category
waits_the_card_to_be_in_category_and_click_on_button_do(browser, wdw, "todo")

# Waits card appear in DOING category
waits_the_card_to_be_in_category_and_click_on_button_do(browser, wdw, "doing")

# Waits card appear in DONE category
waits_the_card_to_be_in_category_and_click_on_button_do(browser, wdw, "done")

# Waits card appear in TODO category again
waits_the_card_to_be_in_category_and_click_on_button_do(browser, wdw, "todo")

# Waits the card appear in DOING category again before quit
waits_the_card_to_be_in_category(wdw, "doing")

browser.quit()


