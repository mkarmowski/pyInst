from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def login_user(browser, username, password):
    browser.get('https://www.instagram.com')

    login_link = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
    if login_link:
        action = ActionChains(browser).move_to_element(login_link).click().perform()

    username_input = browser.find_element_by_xpath \
        ('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/input')
    password_input = browser.find_element_by_xpath \
        ('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/input')

    action = ActionChains(browser).move_to_element(username_input).click().send_keys(username)\
        .move_to_element(password_input).click().send_keys(password).perform()

    login_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button')
    action = ActionChains(browser).move_to_element(login_button).click().perform()
    sleep(5)

    profile_link = browser.find_elements_by_xpath('//a[text()="Profile"]')
    if profile_link:
        return True
    else:
        return False