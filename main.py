import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# system path to chromedriver.exe
CHROMEDRIVER_PATH = r"C:\chromedriver.exe"


def fix_encoding(text):
    try:
        text.decode('utf8', 'strict')
        fixed = text.decode('utf8')
        return fixed
    except UnicodeError:
        pass

    try:
        text.decode('utf16', 'strict')
        fixed = text.decode('utf16')
        return fixed
    except UnicodeError:
        pass

    return text.decode('windows-1256')


text = input("Paste text: ")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH),options=options)

link_to_online_corrector = "https://dadmatech.ir/#/products/SpellChecker"
browser.get(link_to_online_corrector)

text_field = browser.find_element(By.XPATH, '/html/body/div/main/div/div[3]/div[2]/form/div/div/div[1]/div')

# replace the default(testing) text in the field with our text
text_field.send_keys(Keys.CONTROL+'a')
text_field.send_keys(text)

submit_button = browser.find_element(By.XPATH, '/html/body/div/main/div/div[3]/div[2]/form/div/div/div[1]/button')
submit_button.click()

correct_field = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div/div[3]/div[2]/form/div/div/div[3]/div/div[1]')))

corrected_text = fix_encoding(correct_field.text)

print(corrected_text)
