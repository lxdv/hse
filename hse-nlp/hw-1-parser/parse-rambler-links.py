from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from time import sleep
import tqdm
import json

import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('category', type = str, help = "Category, e.g. [politics], [economics], [tech], [starlife]")
parser.add_argument("pages", type = int, help = 'Number of Pages to parse')
parser.add_argument("-o", "--output", type = str, default = 'rambler-news-links.json', help = "File to write links")
args = parser.parse_args()
                    
prefs = {"profile.managed_default_content_settings.images": 2,
         "profile.default_content_settings.cookies": 2}
chrome_options = Options()
chrome_options.add_extension('ext/adblock.crx')
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('--disable-application-cache')
driver = Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.get('chrome-extension://gighmmpiobklfepjocnamgkkbiglidom/options.html')
driver.find_element_by_id('acceptable_ads').click()
driver.find_elements_by_class_name('ui-state-default')[1].click()
driver.implicitly_wait(10)
driver.find_element_by_id('language_select').find_element_by_xpath("//option[@value='russian']").click()
driver.get('https://news.rambler.ru/politics/latest/?page=1')
driver.find_element_by_class_name('j-footer__switch').click()
                    
for page in tqdm.tqdm(range(1, args.pages + 1),position=1):
    driver.get('https://news.rambler.ru/' + args.category + '/latest/?page=' + str(page))
    for element in tqdm.tqdm(driver.find_elements_by_class_name('article-card'),position=0):
        with open(args.output,'a') as file:
                    file.write(json.dumps({
                        'link' : element.find_element_by_tag_name('a').get_attribute('href'),
                        'category': args.category
                    },ensure_ascii=False) + '\n')
driver.quit()