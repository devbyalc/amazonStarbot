from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.amazon.com.au/dp/B08HHV8945/?coliid=I3FP2HRAWVOMOT&colid=QJSJPNI7TG6O&psc=0&ref_=lv_ov_lig_dp_it"
)

# import slack
import os
import slack

client = slack.WebClient(token=os.environ['slack_token'])

import time
while True:
    #check website
    driver.refresh()
    e = driver.find_elements_by_css_selector('input#buy-now-button')
    if e:
        client.chat_postMessage(
            channel='#ps5-bot',
            text=
            "https://www.amazon.com.au/dp/B08HHV8945/?coliid=I3FP2HRAWVOMOT&colid=QJSJPNI7TG6O&psc=0&ref_=lv_ov_lig_dp_it"
        )

    time.sleep(300)
