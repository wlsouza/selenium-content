from selenium.webdriver import Firefox
from time import sleep


# Objective: To generate a dict whose key is "H1" and the value is another dict
# where each key will be the "attribute" value and the value will be the text of the element.


url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

browser = Firefox()
browser.get(url)
sleep(2)

result = {
    "H1":{}
}

paragraphs = browser.find_elements_by_tag_name("p")

for element in paragraphs:
   attribute =  element.get_attribute("atributo")
   result["H1"][attribute]= element.text

print(result)

browser.quit()