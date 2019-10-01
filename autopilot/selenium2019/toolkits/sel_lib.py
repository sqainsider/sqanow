import unittest
import time
import sys,os
import json
from pathlib import Path


sys.path.append('.')
sys.path.append('../toolkits')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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

account_url = "001/o"
oppty_url = "006/o"
order_url = "801/o"
quote_url = "a0q/o"
products_url = "01t/o"
product_rules = "a0j/o"
price_rules = "a0Y/o"
discount_schedules = "a0F/o"



def build_page_object_elements(driver, dataset):
    
    for i in dataset:
        set_elem(driver, dataset[i])


def set_elem(driver,data):
    

    sf_locator_id = data["locator_id"]
    sf_locator_type = data["locator_type"]
    data["driver"] = driver
    
    print(f"data....... {data}")
    time.sleep(data['sleep'])

    if sf_locator_type == "xpath":
        data["element"] =  driver.find_element_by_xpath(sf_locator_id)
    elif sf_locator_type == "id":
        data["element"] =  driver.find_element_by_id(sf_locator_id)
    elif sf_locator_type == "name":
        data["element"] =  driver.find_element_by_name(sf_locator_id)
    elif sf_locator_type == "select":
        # data["element"] = Select(driver.find_element_by_id(sf_locator_id))    
        data["element"] = Select(data["driver"].find_element_by_id(data['locator_id']))

    time.sleep(5)
    if data["processing"] == "now":
        sf_elem_run(data)


def sf_elem_run(data):
    print(f"......... {data}")
    if data["processing"] =='now' or data["processing"] =='defer':
        elem = data["element"]
        method = data["method"]
        value = data["value"]

        if method  == "send_keys":
            elem.send_keys(value)
        elif method == "click":
            elem.click()
        elif method == "select":
            # elem.select_by_visible_text(value) 

            elem = Select(data["driver"].find_element_by_id(data['locator_id']))
            elem.select_by_visible_text(value)


        data["processing"] = "Done"  

        print (data)

def run(dataset):

    # sfdc_driver.maximize_window()
    # Execution
    for i in dataset:
        data = dataset[i]
        print(data)
        sf_elem_run(data)


def screenshot_page(driver, name):

    screenshotDir = " c:\\temp\sfdc\\"
    screenshotfile = ""
    # driver.save_screenshot(r'C:\temp\sfdc\opportunity.png')


def get_sf_base_url(sfdc_url):

    # oppty_url = "https://na112.salesforce.com/0063i000004KFXZ"
    id_index = sfdc_url.find("salesforce.com/")+15
    base_url = sfdc_url[:id_index]
    print(base_url)
    return base_url


def get_object_id(sfdc_url):

    # oppty_url = "https://na112.salesforce.com/0063i000004KFXZ"
    id_index = sfdc_url.find("salesforce.com/")+15
    object_id = sfdc_url[id_index:]
    print(object_id)
    return object_id

# oppty_url = "https://na112.salesforce.com/0063i000004KFXZ"

# opptyid = get_object_id(oppty_url)
# print(opptyid)

# base_url = get_sf_base_url(oppty_url)
# print(base_url)



def login():

    sfdc = webdriver.Chrome("T:\AutoPilot2019\selenium2019\drivers\chromedriver.exe")
    sfdc.implicitly_wait(10)
    url = 'https://login.salesforce.com/'
    #url = 'https://na112.lightning.force.com/lightning/page/home'
    #url_base = 'https://na112.lightning.force.com'
        
    sfdc.get(url)
    sfdc.maximize_window()

    username = 'mycpq_dev@sqanow.com'
    password = 'tiger2019'
    # username = os.environ.get('sfdc_username')
    login_obj = {'username': '', 'password': '', 'login': ''}

    elem1 = sfdc.find_element_by_xpath("//input[@id='username']")
    elem2 = sfdc.find_element_by_xpath("//input[@id='password']")
    elem3 = sfdc.find_element_by_xpath("//input[@id='Login']")

    xpath = "//input[@id='username']"
    login_obj['username'] = elem1
    login_obj['password'] = elem2
    login_obj['login'] = elem3

    login_obj.get('username').send_keys(username)
    login_obj.get('password').send_keys(password)
    login_obj.get('login').click()

    time.sleep(5)

    url = sfdc.current_url


    account_url = "001/o"
    oppty_url = "006/o"
    order_url = "801/o"
    quote_url = "a0q/o"
    products_url = "01t/o"
    product_rules = "a0j/o"
    price_rules = "a0Y/o"
    discount_schedules = "a0F/o"

    oppty_url = get_sf_base_url(url) + oppty_url
    print(oppty_url)
    sfdc.get(oppty_url)

    time.sleep(3)
    locator = "new"
    elem = sfdc.find_element_by_name(locator)
    elem.click()

    # Opportunity Name
    locator = "opp3"
    text = f"QA Daily Check- {timestamp_str()}" 
    elem = sfdc.find_element_by_id(locator)
    elem.send_keys(text)
     

#login()


#print ("done...............")




class SF_Object_Element:

  
    def __init__(self, driver, locator_id, locator_type, method, value):
        self.driver = driver
        self.locator_id = locator_id
        self.locator_type = locator_type
        self.method = method
        self.value = value


    def getElement(self):
        if self.locator_type == 'id':
            elem = "id"
            return elem
        else:
            pass                
 
    def exec(self):
        pass


#elem = SF_Object_Element("d", "locator", "id", "mthd", "text")

#x = elem.getElement()

# exit()




