import unittest
import time
import os


#Selenium
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


#Custom Toolkits
#from toolkit.lib import today

# class AutoPythonOrgSearchLogin(unittest.TestCase):


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Base Dir=:{base_dir}")

drivers_dir =  f"{base_dir}\drivers"

print(drivers_dir)


class Login(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome("T:\AutoPilot2019\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(f"{drivers_dir}\chromedriver.exe")
 

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



        #Opportunity
#        elem = driver.find_element_by_xpath("//a[@title='Opportunities']")
        # elem = driver.find_element_by_xpath("//span[@class='slds-truncate'][contains(text(),'Opportunities')]")
 
        # elem.click()




        # driver.find_element_by_link_text('Opportunities').click
        
        # elem = driver.find_element_by_link_text('Opportunities').click
        
        driver.get('https://na112.lightning.force.com/lightning/o/Opportunity/home')

        elem = driver.find_element_by_link_text('LTE-Product Rule')
        elem.click()

        # elem = driver.find_element_by_partial_link_text('Quotes')
        # elem.click()


        # Opportunity --> Edit
        # xpath = "/html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[1]/a/div"
        xpath = "//div[@title='Edit']"
        elem = driver.find_element_by_xpath(xpath)
        elem.click()

        #Close Date
        # xpath = "//input[@id='5408:0']"
        xpath = "/html[1]/body[1]/div[5]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/article[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"

        value = "10/30/2019"
        elem = driver.find_element_by_xpath(xpath)
        elem.send_keys(value)



        # # Opportuity --> New Quote
        # xpath = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[2]/a/div"
        # elem = driver.find_element_by_xpath(xpath)
        # elem.click()

        # # Opportuity --> Include Document
        # xpath = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[3]/a/div"
        # elem = driver.find_element_by_xpath(xpath)
        # elem.click()

        # # Opportuity --> Create Order
        # xpath = "html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[4]/a/div"
        # elem = driver.find_element_by_xpath(xpath)
        # elem.click()

        # # Dropdown more
        # xpath = '/html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[5]/div/div[1]/div/div/a'
        # elem = driver.find_element_by_xpath(xpath)
        # elem.click()

        # # New Case
        # xpath = "/html/body/div[8]/div/ul/li[1]/a"
        # elem = driver.find_element_by_xpath(xpath)
        # elem.click()





        time.sleep(5)
        # text = f"QA Daily Check-{today()}"
        #elem = driver.find_element_by_link_text('QA Automation-dev1')
        # elem = driver.find_element_by_link_text(text)
        
        # Opportunity --> Quotes
        # elem = driver.find_element_by_xpath('/html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/div/div/div[1]/article/div[2]/header/div[2]/h2/a/span[1]')
        # elem.click()

        # Opportunity --> Edit
        # elem = driver.find_element_by_xpath('/html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[1]/a/div')
        # elem.click()

#    xpath = "//input[@id='username']"

        # xpath = "//input[@id='5847:0']"
        # elem1 = driver.find_element_by_xpath(xpath)

        # xpath = '//input[@id="3592:0"]'
        # elem2 = driver.find_element_by_xpath(xpath)
        
        # # Opportunity --> Edit
        # elem = driver.find_element_by_xpath('/html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[1]/div/header/div[2]/div/div[2]/ul/li[1]/a/div')
        # elem.click()

        # #cancel
        # xpath = '/html/body/div[5]/div[2]/div[8]/div[2]/div/div[3]/div/button[1]/span'
        # elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[8]/div[2]/div/div[3]/div/button[1]/span')
        # elem.click()

        # #Save
        # xpath = '/html/body/div[5]/div[2]/div[8]/div[2]/div/div[3]/div/button[3]/span'
        # elem = driver.find_element_by_xpath(xpath)
      
        # /html/body/div[5]/div[1]/section/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/div/div/div[1]/article/div[2]/header/div[2]/h2/a/span[1]

    def tearDown(self):
        print("Run Successfully")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
