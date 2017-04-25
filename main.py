from datetime import datetime
from modules.like import get_links_by_tag, like_post
from modules.login import login_user
from webdriver.options import chrome_options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class InstaMain:
    def __init__(self, username=None, password=None):
        self.browser = webdriver.Chrome('webdriver/chromedriver', chrome_options=chrome_options)
        self.logs = open('logs/logs.txt', 'a')
        self.logs.write('Started: {}\n'.format(datetime.now().strftime('%d-%m-%Y %H:%M:%S')))

        self.username = username
        self.password = password

    def login(self):
        if login_user(self.browser, self.username, self.password):
            print('Logged in')
            self.logs.write('Logged in\n')
        else:
            print('Not logged in. Wrong user data.')
            self.logs.write('Not logged in. Wrong user data.\n')

        return self

    def like_image(self, tags=None, count=100):
        liked_images = 0
        already_liked = 0
        liked_links = []
        already_liked_links = []

        for index, tag in enumerate(tags):
            print(index), print(tag)
            print('Current tag: {} ({}/{})\n'.format(tag, index + 1, len(tags)))
            self.logs.write('Tag: {} ({}/{})\n'.format(tag, index + 1, len(tags)))

            links = get_links_by_tag(self.browser, tag, count)

            for ind, link in enumerate(links):
                self.logs.write('{}/{}: {}\n'.format(ind + 1, len(links), link))
                print('{}/{}\n'.format(ind + 1, len(links)))
                self.browser.get(link)

                try:
                    liked = like_post(self.browser)

                    if liked:
                        liked_images += 1
                        liked_links.append(link)
                    else:
                        already_liked += 1
                        already_liked_links.append(link)

                except NoSuchElementException:
                    self.logs.write('Invalid Page: {}\n'.format(NoSuchElementException))
                    print('Invalid Page: {}\n'.format(NoSuchElementException))

        self.logs.write('Liked images: {}\n'.format(liked_images))
        self.logs.write('Already liked images: {}\n'.format(already_liked))
        self.logs.write('Links to liked images: {}\n'.format(liked_links))
        self.logs.write('Links to already liked images: {}\n'.format(already_liked_links))
        print('Liked images:\n{}\n'.format(liked_images))
        print('Already liked images:\n{}\n'.format(already_liked))

        return self
