from random import choice
from modules.time import random_sleep


def comment_post(browser, comments):
    random_comment = (choice(comments))
    comment_field = browser.find_element_by_xpath('//input[@placeholder = "Add a comment…"]')
    comment_field.send_keys(random_comment)
    comment_field.submit()
    random_sleep(2)

    return True
