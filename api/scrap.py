from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from liScrapper.person import Person
import liScrapper.actions as actions

import configparser

chrome_options = Options()
# chrome_options.add_argument("--headless") #To hide the browser
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

def scrape_profile(url):
     """
         Scrapes the person's profile
         Parameters:
          url (string): LinkedIn URL sent from the frontend
         Return:
          Json object with person's information
     """

     person = Person(url, driver=driver, close_on_complete = False)
     person_json = person.to_json()
     return person_json


def li_login():
     """
          Log into LinkedIn.
          This function attempts to log into LinkedIn using the provided credentials or cookies in the config file.
          If cookies are provided (recommended), it attempts to log in using the cookie, otherwise email and password will be used
     """
     config = configparser.ConfigParser()
     config.read('config.ini')

     email = config['Default']['email']
     password = config['Default']['password']
     cookie = config['Default']['cookie']

     try:
          if(cookie is not None and cookie != ''):
               actions.login(driver, cookie=cookie)
          elif(email != '' and password != ''):
               actions.login(driver, email=email, password=password)
          else:
               actions.login(driver) #if not provided prompt user
     except:
          raise