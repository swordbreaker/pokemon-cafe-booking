from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

def create_booking(day_of_month: int, month: int, num_of_guests: int):

    website = "https://kirbycafe-reserve.com/guest/tokyo/"

    edge_options = Options()
    edge_options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=edge_options)

    driver.get(website)

    try:
        driver.implicitly_wait(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # agree to terms
        driver.find_element(By.XPATH, "//label[contains(text(), '上記の内容を確認しました')]").click()

        # click on next
        driver.find_element(By.CSS_SELECTOR, "a.v-btn").click()

        # popup click on ok
        driver.find_element(By.CSS_SELECTOR, ".v-card__actions button.v-btn").click()
        
        # number of guests
        driver.find_element(By.CSS_SELECTOR, ".reserve-card .layout div.v-input").click()
        driver.find_element(By.XPATH, "//div[contains(@id, '"+ str(num_of_guests) +"')]").click()

        # select next month
        driver.find_element(By.XPATH, "//button//span[contains(text(), '" + str(month) + "月')]").click()

        # chnage language
        driver.find_element(By.XPATH, "//button//span//span[contains(text(), 'JP')]").click()
        driver.find_element(By.XPATH, "//div//div[contains(text(), 'Eng')]").click()

    except NoSuchElementException as e:
        print(e)
        
num_iterations = 2
next_month=3
day_of_month='10'
num_of_guests=2
[create_booking(day_of_month, next_month, num_of_guests) for x in range(num_iterations)]