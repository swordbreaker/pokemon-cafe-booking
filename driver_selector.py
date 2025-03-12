from selenium import webdriver
from selenium.webdriver.edge.options import Options


def get_driver(driver_name: str):
    '''Get the web driver based on the driver name
    Keyword arguments:
    driver_name -- name of the web driver to use ('chrome', 'edge', 'firefox', 'safari')
    '''
    if driver_name.lower() == "chrome":
        return webdriver.Chrome()
    elif driver_name.lower() == "edge":
        edge_options = Options()
        edge_options.add_experimental_option("detach", True)
        return webdriver.Edge(options=edge_options)
    elif driver_name.lower() == "firefox":
        return webdriver.Firefox()
    elif driver_name.lower() == "safari":
        return webdriver.Safari()
    else:
        raise ValueError(
            "Invalid driver name. Choose 'chrome', 'edge', 'firefox', or 'safari'.")
