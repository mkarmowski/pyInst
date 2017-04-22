from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--dns-prefetch-disable')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--lang=en-US')
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})