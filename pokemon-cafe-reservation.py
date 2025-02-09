from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


def create_booking(day_of_month, num_of_guests, location):
    '''Create a reservation for Pokemon Cafe in Tokyo
    Keyword arguments:
    day_of_month -- day of the month to book
    num_of_guests -- number of guests to book (1-8)
    '''

    if location == "Tokyo":
        website = "https://reserve.pokemon-cafe.jp/"
    elif location == "Osaka":
        website = "https://osaka.pokemon-cafe.jp/"

    edge_options = Options()
    edge_options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=edge_options)

    driver.get(website)

    try:
        driver.implicitly_wait(10)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # 席の予約 HTML 2 - Agree T&C
        # driver.implicitly_wait(10)
        agreeCheck = driver.find_element(By.CSS_SELECTOR, "label.agreeChecked")
        ActionChains(driver).move_to_element(
            agreeCheck).click(agreeCheck).perform()

        # driver.find_element(By.XPATH, "//*[@id='agreeChecked']").click()
        # driver.find_element(By.XPATH, "//*[@class='agreeChecked']").click()
        driver.find_element(By.XPATH, "//*[@class='button']").click()

        driver.find_element(By.CSS_SELECTOR, "a.button").click()

        # 席の予約 HTML 3 - Select number of guest
        select = Select(driver.find_element(By.NAME, 'guest'))
        select.select_by_index(num_of_guests)

        # 席の予約 HTML 4 - Select from calendar
        driver.find_element(
            By.XPATH, "//*[contains(text(), '次の月を見る')]").click()
        driver.implicitly_wait(10)
        # driver.find_element(By.XPATH, "//*[contains(text(), " + str(day_of_month) + ")]").click()
        driver.find_element(
            By.XPATH, "//*[text()=" + str(day_of_month) + "]").click()
        driver.find_element(By.XPATH, "//*[@class='button']").click()
    except NoSuchElementException as e:
        print(e)


num_iterations = 2
day_of_month = '10'
num_of_guests = 2
location = 'Tokyo'
# location = 'Osaka'
[create_booking(day_of_month, num_of_guests, location)
 for x in range(num_iterations)]
