import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .objects import Experience, Education, Scraper, Interest, Accomplishment, Contact
import os
# import selectors


class Person(Scraper):

    __TOP_CARD = "pv-top-card"
    __WAIT_FOR_ELEMENT_TIMEOUT = 50

    def __init__(
        self,
        linkedin_url=None,
        name=None,
        about=None,
        experiences=None,
        educations=None,
        interests=None,
        accomplishments=None,
        company=None,
        job_title=None,
        contacts=None,
        driver=None,
        get=True,
        scrape=True,
        close_on_complete=True,
        time_to_wait_after_login=0,
    ):
        self.linkedin_url = linkedin_url
        self.name = name
        self.about = about or []
        self.experiences = experiences or []
        self.educations = educations or []
        self.interests = interests or []
        self.accomplishments = accomplishments or []
        self.also_viewed_urls = []
        self.contacts = contacts or []

        if driver is None:
            try:
                if os.getenv("CHROMEDRIVER") == None:
                    driver_path = os.path.join(
                        os.path.dirname(__file__), "drivers/chromedriver"
                    )
                else:
                    driver_path = os.getenv("CHROMEDRIVER")

                driver = webdriver.Chrome(driver_path)
            except:
                driver = webdriver.Chrome()

        if get:
            driver.get(linkedin_url)

        self.driver = driver

        if scrape:
            self.scrape(close_on_complete)

    def add_about(self, about):
        self.about.append(about)

    def add_experience(self, experience):
        self.experiences.append(experience)

    def add_education(self, education):
        self.educations.append(education)

    def add_interest(self, interest):
        self.interests.append(interest)

    def add_accomplishment(self, accomplishment):
        self.accomplishments.append(accomplishment)

    def add_location(self, location):
        self.location = location

    def add_contact(self, contact):
        self.contacts.append(contact)

    def scrape(self, close_on_complete=True):
        if self.is_signed_in():
            self.scrape_logged_in(close_on_complete=close_on_complete)
        else:
            print("you are not logged in!")

    def get_img(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, '.pv-top-card--photo-resize img').get_attribute("src")
            # return self.driver.find_element(By.XPATH, "//div[@class='pv-top-card--photo-resize']//img").get_attribute("src")
        except:
            return None

    def get_experiences(self):
        url = os.path.join(self.linkedin_url, "details/experience")
        self.driver.get(url)
        self.focus()
        main = self.wait_for_element_to_load(by=By.TAG_NAME, name="main")
        self.scroll_to_half()
        self.scroll_to_bottom()
        # main_list = self.wait_for_element_to_load(name="pvs-list__container", base=main)
        items = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.pvs-list__paged-list-item')))
        for item in items:
            try:
                company_name_elements  = item.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal > span:first-child')
                company_name = company_name_elements.text if company_name_elements else "" 
            except:
                company_name = ''
                continue
            try:
                position = item.find_element(By.CSS_SELECTOR, 'div.t-bold > span:first-child')
                position = position.text if position else ""
            except: 
                position = ''
                continue
            try:
                dates = item.find_element(By.CSS_SELECTOR, 'span.pvs-entity__caption-wrapper').text 
            except:
                dates = ''
                continue
            try: 
                details = item.find_element(By.CSS_SELECTOR, 'div.t-14.t-normal.t-black > span:first-child').text
            except:
                details = ''
                continue

            experience = {
                "company_name": company_name, 
                "position": position, 
                "details": details, 
                "dates": dates
            }
            self.add_experience(experience)

    def get_educations(self):
        url = os.path.join(self.linkedin_url, "details/education")
        self.driver.get(url)
        self.focus()
        main = self.wait_for_element_to_load(by=By.TAG_NAME, name="main")
        self.scroll_to_half()
        self.scroll_to_bottom()
        items = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.pvs-list__paged-list-item')))
        for item in items:
            # degree_elements  = item.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal > span:first-child')
            # degree = degree_elements.text if degree_elements else "" 

            # university_elems = item.find_element(By.CSS_SELECTOR, 'div.t-bold > span:first-child')
            # university = university_elems.text if university_elems else ""
            # dates = item.find_element(By.CSS_SELECTOR, 'span.pvs-entity__caption-wrapper').text 
            try:
                company_name_elements  = item.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal > span:first-child')
                company_name = company_name_elements.text if company_name_elements else "" 
            except:
                company_name = ''
                continue
            try:
                position = item.find_element(By.CSS_SELECTOR, 'div.t-bold > span:first-child')
                position = position.text if position else ""
            except: 
                position = ''
                continue
            try:
                dates = item.find_element(By.CSS_SELECTOR, 'span.pvs-entity__caption-wrapper').text 
            except:
                dates = ''
                continue
            education = {
                "university": company_name, 
                "degree": position, 
                "dates": dates 
            }

            self.add_education(education)

    def get_name_and_location(self):
        top_panel = self.driver.find_element(By.XPATH, "//*[@class='mt2 relative']")
        try:
            self.name = top_panel.find_element(By.TAG_NAME, "h1").text
        except:
            self.name = 'Unknown'
        try:
            self.location = top_panel.find_element(By.XPATH, "//*[@class='text-body-small inline t-black--light break-words']").text
        except:
            self.location = 'Unknown'
      
    def scrape_logged_in(self, close_on_complete=True):
        driver = self.driver
        duration = None

        self.focus()
        self.wait(5)

        # get name and location
        self.get_name_and_location()

        self.img = self.get_img()

        # get about
        # self.get_about()
        driver.execute_script(
            "window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));"
        )
        driver.execute_script(
            "window.scrollTo(0, Math.ceil(document.body.scrollHeight/1.5));"
        )

        # get experience
        self.get_experiences()

        # get education
        self.get_educations()

        driver.get(self.linkedin_url)

        if close_on_complete:
            driver.quit()

    @property
    def company(self):
        if self.experiences:
            return (
                self.experiences[0].institution_name
                if self.experiences[0].institution_name
                else None
            )
        else:
            return None

    @property
    def job_title(self):
        if self.experiences:
            return (
                self.experiences[0].position_title
                if self.experiences[0].position_title
                else None
            )
        else:
            return None

    def __repr__(self):
        return json.dumps({
            "name": self.name,
            "location": self.location,
            "img": self.img,
            "experience": self.experiences,
            "education": self.educations,
        })

        # return "<Person {name}\n\nAbout\n{about}\n\nExperience\n{exp}\n\nEducation\n{edu}\n\nInterest\n{int}\n\nAccomplishments\n{acc}\n\nContacts\n{conn}>".format(
        #     name=self.name,
        #     location=self.location,
        #     img=self.img,
        #     exp=self.experiences,
        #     edu=self.educations,
        # )

    def to_json(self):
        return {
            "name": self.name,
            "location": self.location,
            "img": self.img,
            "experience": self.experiences,
            "education": self.educations,
        }
