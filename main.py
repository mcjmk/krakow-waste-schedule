import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

STREET_NAME = "Rynek Główny"
HOUSE_NUMBER = "1"

URL = "https://mpo.krakow.pl/harmonogram-odbioru/"
driver = webdriver.Firefox()
driver.get(URL)

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500)")

iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "iframe[src='https://harmonogram.mpo.krakow.pl']")
    )
)
driver.switch_to.frame(iframe)

select_street_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "select2-sel_ulice-container"))
)
select_street_element.click()

search_street_input = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='search'][autocomplete='off'][role='textbox'].select2-search__field",
)
search_street_input.clear()
search_street_input.send_keys(STREET_NAME)

search_street_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input.select2-search__field[type='search']")
    )
)
street_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-results__option"))
)
street_result.click()


select_number_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "select2-sel_numer-container"))
)
select_number_element.click()

search_number_input = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='search'][autocomplete='off'][role='textbox'].select2-search__field",
)
search_number_input.clear()
search_number_input.send_keys(HOUSE_NUMBER)

search_number_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input.select2-search__field[type='search']")
    )
)
number_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-results__option"))
)
number_result.click()

get_pdf_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "get_pdf"))
)
get_pdf_button.click()

driver.quit()
