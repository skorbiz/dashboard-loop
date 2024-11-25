
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless") # This dosnt work for whatever reason options.headless = True
options.add_argument("--window-size=1200,1920")

driver = webdriver.Chrome(options=options)
driver.get('https://www.wired.com/tag/robotics/')

# Click the accept user agreement button and wait for fade effect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

accept_button = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
accept_button.click()
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located(accept_button))

# Take screenshot and close
driver.save_screenshot('test.png')
driver.close()
exit(0)

# More selenium documentation:
# https://selenium-python.readthedocs.io/waits.html




# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options

# options = FirefoxOptions()
# # Workaround fore firefox profile (Not needed for chrome driver)
# options.add_argument("-profile")
# # put the root directory your default profile path here, you can check it by opening Firefox and then pasting 'about:profiles' into the url field 
# options.add_argument("/home/johl/snap/firefox/common/.mozilla/firefox/cq096zca.selenium")
# service = Service('/usr/local/bin/geckodriver')
# driver = webdriver.Firefox(options=options, service=service)
# driver.get('https://www.wired.com/tag/robotics/')

# driver.get_full_page_screenshot_as_file('example.png')