import os
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
browser = webdriver.Chrome(
    executable_path="./webdriver/chromedriver",
    options=options
)

# URL to translate file names.
url = "https://translate.google.com/?ui=tob&sl=auto&tl=en&op=translate"
# URL to translate text files.
url_docs = "https://translate.google.com/?ui=tob&sl=auto&tl=en&op=docs"

text_files = os.listdir("./data/компьютеры/")
for text_file in text_files:
    print(text_file)
    browser.get(url)
    text_data = open(f"./data/компьютеры/{text_file}", "r").read()

    input_area = browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/'
        'c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea'
    )
    input_area.click()
    time.sleep(1)
    input_area.send_keys(text_file.replace(".txt", "").replace("_", " "))
    time.sleep(1)

    file_name = browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/'
        'c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/'
        'div/div[1]/span[1]/span/span'
    ).text.replace(" ", "_")

    browser.get(url_docs)
    file_input = browser.find_element_by_xpath(
        '//*[@id="i34"]'
    )
    file_input.send_keys(
        f"/home/alexander/projects/misc/translate/data/компьютеры/{text_file}"
    )
    time.sleep(1)

    translate_button = browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[2]/c-wiz/'
        'div/form/div[2]/div[2]/button/span'
    )
    translate_button.click()
    sleep_time = random.choice(range(10, 30))
    print(f"Waiting {str(sleep_time)} seconds...")
    time.sleep(sleep_time)
    text = str(browser.find_element_by_tag_name(
        "pre"
    ).get_attribute("innerHTML").replace("&lt;", "<").replace("&gt;", ">"))

    with open(f"./results/it/{file_name}.txt", "w+") as new_file:
        new_file.write(text)

    os.remove(f"./data/компьютеры/{text_file}")
    print("--- --- ---")

browser.quit()
