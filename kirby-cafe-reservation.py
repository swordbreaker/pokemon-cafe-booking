from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import argparse


def create_booking(num_of_guests: int):
    '''Create a reservation for Kirby Cafe in Tokyo
    Keyword arguments:
    month -- month to book
    num_of_guests -- number of guests to book
    '''
    website = "https://kirbycafe-reserve.com/guest/tokyo/"
    edge_options = Options()
    edge_options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=edge_options)
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

    parser = argparse.ArgumentParser(
        description='Create a reservation for Kirby Cafe.')
    parser.add_argument('--num_of_guests', type=int,
                        help='Number of guests to book', default=num_of_guests, required=False)
    parser.add_argument('--iterations', type=int,
                        help='Number of iterations to run the booking', default=iterations, required=False)

    args = parser.parse_args()

    for _ in range(args.iterations):
        create_booking(args.num_of_guests)
