from math import ceil
from modules.time import random_sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def get_links_by_tag(browser, tag, count):
    """Likes posts by specified tag. Tags must be passed as list"""

    browser.get('https://www.instagram.com/explore/tags/' + (tag[1:] if tag[:1] == '#' else tag))

    body = browser.find_element_by_tag_name('body')
    stop = True
    try:
        load_more = body.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/a')
    except:
        print('Load more button not found')
    else:
        stop = False
        body.send_keys(Keys.END)
        random_sleep(2)
        load_more.click()
    body.send_keys(Keys.HOME)

    main_tag = browser.find_element_by_tag_name('main')
    link_tags = main_tag.find_elements_by_tag_name('a')
    links_count = len(link_tags)
    links = [link.get_attribute('href') for link in link_tags]

    if (links_count < count) and not stop:
        count_left = count - links_count
        new_page_needed = ceil(count_left / 12)

        for i in range(new_page_needed):
            starting_count = links_count
            body.send_keys(Keys.END)
            random_sleep(2)
            body.send_keys(Keys.HOME)
            random_sleep(2)
            link_tags = main_tag.find_elements_by_tag_name('a')
            links_count = len(link_tags)
            stop = (starting_count == links_count)
            if stop:
                break

    links = [link.get_attribute('href') for link in link_tags]

    return links[:count]


def like_post(browser):
    try:
        like_button = browser.find_elements_by_xpath("//a[@role = 'button']/span[text()='Like']")
    except:
        like_button = []
    try:
        unlike_button = browser.find_elements_by_xpath("//a[@role = 'button']/span[text()='Unlike']")
    except:
        unlike_button = []

    if like_button:
        action = ActionChains(browser).move_to_element(like_button[0]).click().perform()
        print('Image liked')
        random_sleep(2)
        return True
    elif unlike_button:
        print('Image already liked')
        random_sleep(2)
        return False
    else:
        print('Cannot find like button')
        random_sleep(2)
        return False
