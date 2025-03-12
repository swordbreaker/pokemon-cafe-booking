from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import argparse
from driver_selector import get_driver


def create_booking(num_of_guests: int, driver_name: str):
    '''Create a reservation for Kirby Cafe in Tokyo
    Keyword arguments:
    num_of_guests -- number of guests to book
    driver_name -- name of the web driver to use ('chrome', 'edge', 'firefox', 'safari')
    '''
    website = "https://kirbycafe-reserve.com/guest/tokyo/"
    driver = get_driver(driver_name)
    driver.get(website)

    try:
        driver.implicitly_wait(10)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Agree to terms
        driver.find_element(
            By.XPATH, "//label[contains(text(), '上記の内容を確認しました')]").click()

        # Click on next
        driver.find_element(By.CSS_SELECTOR, "a.v-btn").click()

        # Popup click on ok
        driver.find_element(
            By.CSS_SELECTOR, ".v-card__actions button.v-btn").click()

        # Number of guests
        driver.find_element(
            By.CSS_SELECTOR, ".reserve-card .layout div.v-input").click()

        guest_option_xpath = f"//div[contains(@id, '{num_of_guests}名様-list-item')]"
        driver.find_element(By.XPATH, guest_option_xpath).click()

    except NoSuchElementException as e:
        print(e)


if __name__ == "__main__":
    # Default parameters
    num_of_guests = 2
    iterations = 1
    driver_name = 'edge'

    parser = argparse.ArgumentParser(
        description='Create a reservation for Kirby Cafe.')
    parser.add_argument('--num_of_guests', type=int,
                        help='Number of guests to book', default=num_of_guests, required=False)
    parser.add_argument('--iterations', type=int,
                        help='Number of iterations to run the booking', default=iterations, required=False)
    parser.add_argument('--driver', type=str, choices=[
                        'chrome', 'edge', 'firefox', 'safari'], help='Web driver to use (chrome, edge, firefox, or safari)', default=driver_name, required=False)

    args = parser.parse_args()

    for _ in range(args.iterations):
        create_booking(args.num_of_guests, args.driver)
