from datetime import datetime
from random import randint

from modules.comment import comment_post
from modules.follow import follow
from modules.like import get_links_by_tag, like_post, verify_post
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

        self.post_comments = False
        self.comment_percentage = 0
        self.comments = []

        self.allow_following = False
        self.follow_percentage = 0
        self.do_not_follow = []         # TODO following restrictions

        self.ignore_users = []
        self.ignore_tags = []
        self.ignore_description = []

    def login(self):
        if login_user(self.browser, self.username, self.password):
            print('Logged in')
            self.logs.write('Logged in\n')
        else:
            print('Not logged in. Wrong user data.')
            self.logs.write('Not logged in. Wrong user data.\n')

        return self

    def set_post_comments(self, on=False, percentage=0):
        self.post_comments = on
        self.comment_percentage = percentage

        return self

    def set_comments(self, comments=None):
        self.comments = comments or []

        return self

    def set_allow_following(self, on=False, percentage=0):
        self.allow_following = on
        self.follow_percentage = percentage

        return self

    def set_do_not_follow(self, names=None):
        self.do_not_follow = names or []

        return self

    def set_ignore_users(self, users=None):
        self.ignore_users = users or []

        return self

    def set_ignore_tags(self, tags=None):
        self.ignore_tags = tags or []

        return self

    def set_ignore_description(self, words=None):
        self.ignore_description = words or []

        return self

    def like_image(self, tags=None, count=100):
        liked_images = 0
        already_liked = 0
        ignored_images = 0
        commented = 0
        liked_links = []
        already_liked_links = []
        commented_links = []

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
                    is_ignored, reason, user_name = verify_post(self.browser, link, self.ignore_users,
                                                     self.ignore_tags, self.ignore_description)

                    if not is_ignored:
                        liked = like_post(self.browser)
                        if liked:
                            liked_images += 1
                            liked_links.append(link)
                            commenting = randint(0, 100) <= self.comment_percentage

                            if self.post_comments and commenting:
                                comment_post(self.browser, self.comments)
                                commented += 1
                                commented_links.append(link)
                                print('Commented on post: {}'.format(link))

                            if self.allow_following:
                                follow(self.browser)

                        else:
                            already_liked += 1
                            already_liked_links.append(link)
                    else:
                        print('Image not liked: {} - {}'. format(link, reason))
                        ignored_images += 1

                except NoSuchElementException:
                    self.logs.write('Invalid Page: {}\n'.format(NoSuchElementException))
                    print('Invalid Page: {}\n'.format(NoSuchElementException))

        self.logs.write('Liked images: {}\n'.format(liked_images))
        self.logs.write('Already liked images: {}\n'.format(already_liked))
        self.logs.write('Images ignored: {}\n'.format(ignored_images))
        self.logs.write('Links to liked images: {}\n'.format(liked_links))
        self.logs.write('Links to already liked images: {}\n'.format(already_liked_links))
        print('Liked images:\n{}\n'.format(liked_images))
        print('Already liked images:\n{}\n'.format(already_liked))
        print('Images ignored:\n{}\n'.format(ignored_images))

        return self

    def quit(self):
        self.browser.delete_all_cookies()
        self.browser.close()

        print('Finished')
        self.logs.write('Finished: {}\n'.format(datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
        self.logs.write('---' * 10 + '\n\n\n')
        self.logs.close()
