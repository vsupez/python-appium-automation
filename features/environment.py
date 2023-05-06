from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def mobile_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """

    # s = Service('C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
    # context.driver = webdriver.Chrome(service=s)

    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(
        executable_path='C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver',
        chrome_options=chrome_options)

    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    mobile_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context):
    context.driver.quit()
