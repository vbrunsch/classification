
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#wait = WebDriverWait(driver, 10)

with webdriver.Firefox() as driver:
    driver.get("https://data.gov.il/dataset/covid-19/resource/8a21d39d-91e3-40db-aca1-f73f7ab1df69/view/58688c13-ad90-4e4c-98c6-e5ee53fe1b2f")
    '''
    driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)

    wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>a")))

    results = driver.find_elements_by_css_selector("h3>a")
    for i, result in results.iteritems():
        print("#{}: {} ({})".format(i, result.text, result.get_property("href")))
    '''
