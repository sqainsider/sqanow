import unittest
import time
import sys,os

sys.path.append('.')
sys.path.append('../toolkits')


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

from toolkits.lib import today


# dirBase = "c:\\myGoogleDrive\\Automation\\Tomato\\AutoPilot2019\\selenium2019\\toolkit\\"
# sys.path.append(os.path.abspath(dirBase))


class Login(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("T:\AutoPilot2019\selenium2019\drivers\chromedriver.exe")
 

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
        

        # Classic Home Page
        url = "https://na112.salesforce.com/home/home.jsp"
        driver.get(url)
        driver.save_screenshot(r'C:\temp\sfdc\login.png')

      
        #Accounts
        # =====================================================================
        driver.get("https://na112.salesforce.com/001/o")

        time.sleep(5)
        locator = "new"
        elem = driver.find_element_by_name(locator)
        elem.click()

        # Opportunity Name
        locator = "opp3"
        text = f"QA Daily Check- {today()}" 
        elem = driver.find_element_by_id(locator)
        elem.send_keys(text)
     
        # Account Name
        locator = "opp4"
        text = "LTE"
        elem = driver.find_element_by_id(locator)
        elem.send_keys(text)
     
        # Close Date
        locator = "opp9"
        text = "09/30/2019"
        elem = driver.find_element_by_id(locator)
        elem.send_keys(text)
     

        # Stage
        locator = "opp11"
        text = "Qualification"
        elem = Select(driver.find_element_by_id(locator))
        elem.select_by_visible_text(text)

        # Save Button
        locator = "save"
        elem = driver.find_element_by_name(locator)
        elem.click()
    
        
        driver.save_screenshot(r'C:\temp\sfdc\account.png')


        # elem = driver.find_element_by_link_text('LTE-Product Rule')
        # elem.click()

        # elem = driver.find_element_by_partial_link_text('Quotes')
        # elem.click()


        # Related Links
        # =====================================================================
        # Opportuity --> Contact Roles
        # locator = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[3]/a/div"
        # elem = driver.find_element_by_xpath(locator)
        # elem.click()

     
        # Opportuity --> Quote
        # locator = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[3]/a/div"
        # elem = driver.find_element_by_xpath(locator)
        # elem.click()

        # # Opportuity --> Product
        # locator = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[4]/a/div"
        # elem = driver.find_element_by_xpath(locator)
        # elem.click()

        # # Opportuity --> Quote Documents
        # locator = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[4]/a/div"
        # elem = driver.find_element_by_xpath(locator)
        # elem.click()


        # # Opportuity --> Contract
        # locator = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[4]/a/div"
        # elem = driver.find_element_by_xpath(locator)
        # elem.click()

        # # Opportuity --> Renewal Contract
        # locator = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[4]/a/div"
        # elem = driver.find_element_by_xpath(locator)
        # elem.click()


        # # Opportuity --> Note & Attachments
        # locator = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[4]/a/div"
        # elem = driver.find_element_by_xpath(locator)
        # elem.click()

        # Buttons
        # =====================================================================
        # Opportunity --> Edit
        time.sleep(5)
        locator = "edit"
        elem = driver.find_element_by_name(locator)
        elem.click()

        locator = "opp14"
        text = "The oppty is created by script"
        elem = driver.find_element_by_id(locator)
        elem.send_keys(text)


        locator = "save"
        elem = driver.find_element_by_name(locator)
        elem.click()


        # locator = "save_new"
        # elem = driver.find_element_by_name(locator)
        # elem.click()


        # locator = "cancel"
        # elem = driver.find_element_by_name(locator)
        # elem.click()





        #      # 
        # 
        # Delete
        # Include Document
        # Create Order




        time.sleep(3)
 

    def tearDown(self):
        print("Run Successfully")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
