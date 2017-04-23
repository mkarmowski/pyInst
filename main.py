from datetime import datetime
from modules.login import login_user
from webdriver.options import chrome_options
from selenium import webdriver


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
