from base.selenium_base import Selenium_base
from utilities import custom_logging as cl
import logging


class Confirm(Selenium_base):
    log = cl.log(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    dropdownc = "//select"
    checkboxt = ".chkAgree"
    proceed = "//button[text()='Proceed']"
    search = "//input[@type='search']"

    def selectCountry(self, text):
        self.selectdropdownvaluebyvisibletext(self.dropdownc, text, "xpath")

    def clickcheck(self):
        self.clickelement(self.checkboxt,"css")

    def clickProceed(self):
        self.clickelement(self.proceed, "xpath")

    def validateconfirmation(self):
        confirmy=self.validatepresence(self.search, "xpath")
        if confirmy == "True":
            return True
        else:
            return False



    def submittransaction(self, text):
        self.selectCountry(text)
        self.clickcheck()
        self.clickProceed()




