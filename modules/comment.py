from random import choice
from time import sleep


def comment_post(browser, comments):
    random_comment = (choice(comments))
    comment_field = browser.find_element_by_xpath('//input[@placeholder = "Add a comment…"]')
    comment_field.send_keys(random_comment)
    comment_field.submit()
    sleep(1)

    return True
