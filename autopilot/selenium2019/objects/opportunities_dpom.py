import unittest
import time
import sys,os
import json
from pathlib import Path

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
sys.path.append('.')
sys.path.append("../toolkits")

print(sys.path)

from toolkits.lib import today, timestamp_str
from toolkits.sel_lib import get_object_id, get_sf_base_url 
from toolkits.sel_lib import build_page_object_elements, run


driver_dir = f"{base_dir}\drivers"

# class Login(unittest.TestCase):
json_dir = driver_dir = f"{base_dir}\json"


# json_src_data = Path("C:\myGoogleDrive\Automation\Tomato\AutoPilot2019\selenium2019\json\SF_Elements_Repo.json").read_text()
json_src_data = Path(f"{json_dir}\json\SF_Elements_Repo.json").read_text()

json_data = json.loads(json_src_data)
sfdc_login = json_data["Login"]
sfdc_opportunity = json_data["Opportunites"]

  
# sfdc_driver = webdriver.Chrome("C:\myGoogleDrive\Automation\Tomato\AutoPilot2019\selenium2019\drivers\chromedriver.exe")
sfdc_driver = webdriver.Chrome(f"{driver_dir}\chromedriver.exe")

# sfdc = self.driver
sfdc_driver.implicitly_wait(10)
url = 'https://login.salesforce.com/'
# url = 'https://na112.lightning.force.com/lightning/page/home'
# url_base = 'https://na112.lightning.force.com'
sfdc_driver.get(url)
sfdc_driver.minimize_window()


# Login
# *****************************************************************************
build_page_object_elements(sfdc_driver, sfdc_login)
run(sfdc_login)

# Opportunity
# *****************************************************************************
sfdc_driver.get("https://na112.salesforce.com/006/o")

print ("Opportunties")
print (sfdc_opportunity)

build_page_object_elements(sfdc_driver, sfdc_opportunity)
run(sfdc_opportunity)

get_object_id(sfdc_driver.current_url)


exit()
