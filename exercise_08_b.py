from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from json import loads

# Objective: trigger all events that change the color of the box and print all colors.
# There's a bug with the page that does not consider double-clicking if the control key is pressed. (2 colors)
# Context_click is considered only if the control or shift keys are not pressed. (3 colors)
# The total colors excluding the bugs are: 15  (20 - 2 - 3)



# Just playing with the concept of wrappers and using that like as partial of the functools...
# and yes, I know that I'm complicating it unnecessarily, it's just for fun. ¯\_(ツ)_/¯
def pressed_key(func, key):
    def wrapper(*args,**kwargs):
        ac = None
        for arg in args + tuple(kwargs.values()):
            if type(arg) == ActionChains:
                ac = arg 
                break
        if ac:
            ac.key_down(key)
            func(*args, **kwargs)
            ac.key_up(key)
        return None
    return wrapper

def do_actions_on_box(browser, action_chains):
    box = browser.find_element_by_id("caixa")
    action_chains.move_to_element(box)
    action_chains.click()
    action_chains.context_click()
    action_chains.double_click()
    action_chains.move_to_element(browser.find_element_by_tag_name("h1"))
    action_chains.perform()

url = "https://selenium.dunossauro.live/exercicio_08.html"

browser = Firefox()
browser.get(url)
sleep(1)

ac = ActionChains(browser)

do_actions_pressed_shift = pressed_key(do_actions_on_box, Keys.SHIFT)
do_actions_pressed_ctrl = pressed_key(do_actions_on_box, Keys.CONTROL)
do_actions_pressed_shift_and_ctrl = pressed_key(do_actions_pressed_shift, Keys.CONTROL)

do_actions_on_box(browser, ac)
do_actions_pressed_shift(browser, ac)
do_actions_pressed_ctrl(browser, ac)
do_actions_pressed_shift_and_ctrl(browser, ac)


area_text = browser.find_element_by_id("area").text
# putting double quotes in the keys
area_text = area_text.replace("{" , "{\"")
area_text = area_text.replace(", " , ", \"")
area_text = area_text.replace(":" , "\":")
area_text = area_text.lower()

rows = area_text.split("\n")

colors = set()
for row in rows:
    colors.add(
        loads(row).get("cor")
    )

print(f"qtd:{len(colors)}, colors:{colors}")