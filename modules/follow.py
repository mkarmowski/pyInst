from modules.time import random_sleep


def follow(browser):
    follow_button = browser.find_element_by_xpath("//article/header/span/button")
    random_sleep(2)

    if follow_button.text == 'Follow':
        follow_button.click()
        print('Following\n')
        return True

    else:
        print('Already following\n')
        return False
