from time import sleep


def follow(browser):
    follow_button = browser.find_element_by_xpath("//article/header/span/button")
    sleep(1)

    if follow_button.text == 'Follow':
        follow_button.click()
        print('Following\n')
        return True

    else:
        print('Already following\n')
        return False
