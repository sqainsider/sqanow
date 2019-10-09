import unittest
import time
import sys,os

sys.path.append('.')
sys.path.append('../toolkits')

# print(sys.path)
# dirBase = "c:\\myGoogleDrive\\Automation\\Tomato\\AutoPilot2019\\selenium2019\\toolkits\\"
# sys.path.append(os.path.abspath(dirBase))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# from customer import account

# from selenium import alert
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.alert import Alert

# Custom
from toolkits.lib import today, timestamp_str
from toolkits.sel_lib import get_object_id, get_sf_base_url


class Login(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("T:\AutoPilot2019\selenium\drivers\chromedriver.exe")
 

    def test_run(self):

        driver = self.driver
        driver.implicitly_wait(10)
        #url = 'https://login.salesforce.com/'
        url = 'https://na112.lightning.force.com/lightning/page/home'
        url_base = 'https://na112.lightning.force.com'
        driver.get(url)
        driver.maximize_window()

        username = 'mycpq_dev@sqanow.com'
        password = 'tiger2019'
        # username = os.environ.get('sfdc_username')
        login_obj = {'username': '', 'password': '', 'login': ''}

        elem1 = driver.find_element_by_xpath("//input[@id='username']")
        elem2 = driver.find_element_by_xpath("//input[@id='password']")
        elem3 = driver.find_element_by_xpath("//input[@id='Login']")

        xpath = "//input[@id='username']"
        login_obj['username'] = elem1
        login_obj['password'] = elem2
        login_obj['login'] = elem3

        login_obj.get('username').send_keys(username)
        login_obj.get('password').send_keys(password)
        login_obj.get('login').click()

        time.sleep(5)
        driver.save_screenshot(r'C:\temp\sfdc\login.png')


    def tearDown(self):
        print("Run Successfully")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
