from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import argparse
from driver_selector import get_driver


def create_booking(day_of_month: int, num_of_guests: int, location: str, driver_name: str):
    '''Create a reservation for Pokemon Cafe in Tokyo or Osaka
    Keyword arguments:
    day_of_month -- day of the month to book
    num_of_guests -- number of guests to book (1-8)
    location -- location of the cafe ('Tokyo' or 'Osaka')
    driver_name -- name of the web driver to use ('chrome', 'edge', 'firefox', 'safari')
    '''
    if location == "Tokyo":
        website = "https://reserve.pokemon-cafe.jp/"
    elif location == "Osaka":
        website = "https://osaka.pokemon-cafe.jp/"
    else:
        raise ValueError("Invalid location. Choose 'Tokyo' or 'Osaka'.")

    driver = get_driver(driver_name)
    driver.get(website)

    try:
        driver.implicitly_wait(10)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Agree to terms and conditions
        agreeCheck = driver.find_element(By.CSS_SELECTOR, "label.agreeChecked")
        ActionChains(driver).move_to_element(
            agreeCheck).click(agreeCheck).perform()

        # Click on the next button
        driver.find_element(By.XPATH, "//*[@class='button']").click()

        # Wait for user to solve CAPTCHA
        print("Please solve the CAPTCHA...")
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@class='button arrow-down' and @href='/reserve/step1']"))
        )

        # Proceed after CAPTCHA is solved
        driver.find_element(
            By.XPATH, "//a[@class='button arrow-down' and @href='/reserve/step1']").click()

        # Select number of guests
        select = Select(driver.find_element(By.NAME, 'guest'))
        select.select_by_index(num_of_guests)

        # Select the day from the calendar
        driver.find_element(
            By.XPATH, "//*[contains(text(), '次の月を見る')]").click()
        driver.implicitly_wait(10)
        driver.find_element(
            By.XPATH, "//*[text()=" + str(day_of_month) + "]").click()
        driver.find_element(By.XPATH, "//*[@class='button']").click()
    except NoSuchElementException as e:
        print(e)


if __name__ == "__main__":

    # Default values
    num_iterations = 2
    next_month = 3
    day_of_month = '10'
    num_of_guests = 2
    location = 'Tokyo'
    driver_name = 'edge'

    parser = argparse.ArgumentParser(
        description='Create a reservation for Pokemon Cafe.')
    parser.add_argument('--day_of_month', type=int,
                        help='Day of the month to book', default=day_of_month, required=False)
    parser.add_argument('--num_of_guests', type=int,
                        help='Number of guests to book (1-8)', default=num_of_guests, required=False)
    parser.add_argument('--location', type=str, choices=[
                        'Tokyo', 'Osaka'], help='Location of the cafe (Tokyo or Osaka)', default=location, required=False)
    parser.add_argument('--iterations', type=int,
                        help='Number of iterations to run the booking', default=num_iterations, required=False)
    parser.add_argument('--driver', type=str, choices=[
                        'chrome', 'edge', 'firefox', 'safari'], help='Web driver to use (chrome, edge, firefox, or safari)', default=driver_name, required=False)

    args = parser.parse_args()

    for _ in range(args.iterations):
        create_booking(args.day_of_month, args.num_of_guests,
                       args.location, args.driver)
