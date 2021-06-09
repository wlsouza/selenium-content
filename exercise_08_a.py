import pyautogui
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# Objective: Send to page a normal text, a text with the shift
# pressed, a text with the capslock pressed and a text with both pressed. 
# The method reset_actions has a bug related here: https://github.com/SeleniumHQ/selenium/issues/6837


url = "https://curso-python-selenium.netlify.app/aula_08_a.html"

browser = Firefox()
browser.get(url)
sleep(1)

ac = ActionChains(browser)

text_area = browser.find_element_by_tag_name("textarea")

def send_hello_world(ac, element):
    ac.pause(1)
    ac.move_to_element(element)
    ac.click()
    ac.send_keys("hello world")
    ac.perform()
    ac.reset_actions()
    # bug fix 
    for device in ac.w3c_actions.devices:
        device.clear_actions()

# normal
send_hello_world(ac, text_area)

# with shift
ac.key_down(Keys.SHIFT)
send_hello_world(ac, text_area)

# with caps 
# (it's not possible with selenium (https://github.com/seleniumhq/selenium-google-code-issue-archive/issues/785),
# so I used pyautogui to press the capslock key and write)
# I tried press caps lock with pyautogui and write with selenium but the selenium doesn't respect caps lock (I don't know why)
# I also tried researching how to send the control modifier to the w3c keypress event using selenium but was unsuccessful. 
pyautogui.press("capslock")
pyautogui.write("hello world")
pyautogui.press("capslock")