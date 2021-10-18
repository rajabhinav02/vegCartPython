import logging
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import utilities.custom_logging as cl

class Selenium_base:
    log = cl.log(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getBytype(self, locatortype):
        try:
            if locatortype is not None:
                locatortype = locatortype.lower()
                if locatortype == "id":
                    self.log.info("locatortype "+locatortype + " has been returned")
                    return By.ID
                elif locatortype == "xpath":
                    self.log.info("locatortype " + locatortype + " has been returned")
                    return By.XPATH
                elif locatortype == "css":
                    self.log.info("locatortype " + locatortype + " has been returned")
                    return By.CSS_SELECTOR
                elif locatortype == "name":
                    self.log.info("locatortype " + locatortype + " has been returned")
                    return By.NAME
                elif locatortype == "class":
                    self.log.info("locatortype " + locatortype + " has been returned")
                    return By.CLASS_NAME
                elif locatortype == "link":
                    self.log.info("locatortype " + locatortype + " has been returned")
                    return By.LINK_TEXT
            else:
                self.log.error("No locatortype returned")
        except:
            self.log.error("No locatortype returned")


    def getelement(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            bytype = self.getBytype(locatortype)
            element = self.driver.find_element(bytype, locator)
            self.log.info("element returned with locator "+locator + " and locatortype "+locatortype)
            return element
        except:
            self.log.error("no element returned with locator "+locator + " and locatortype "+locatortype)

    def getelementlist(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            bytype = self.getBytype(locatortype)
            elementlist = self.driver.find_elements(bytype, locator)
            self.log.info("elementlist returned with locator " + locator + " and locatortype " + locatortype)
            return elementlist
        except:
            self.log.error("no elementlist returned with locator " + locator + " and locatortype " + locatortype)

    def clickelement(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locator, locatortype)
            element.click()
            self.log.info("element with locator " + locator + " and locatortype " + locatortype +" clicked")
        except:
            self.log.error("element with locator " + locator + " and locatortype " + locatortype +" not clicked")

    def senddata(self, data, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locator, locatortype)
            element.send_keys(data)
            self.log.info("data " + data +" send to element with locator " + locator + " and locatortype " + locatortype)
        except:
            self.log.error("data " + data +" not send to element with locator " + locator + " and locatortype " + locatortype)

    def getxpathfromchild(self, child, locator):
        try:
            bytype = self.getBytype("xpath")
            xpathchild = child.find_element(bytype,locator)
            self.log.info("xpath returned from child for locator "+locator + " is returned")
            return xpathchild
        except:
            self.log.error("xpath returned from child for locator "+locator + " is not returned")

    def waitforpresence(self, time, locator, locatortype="id"):
        try:
            locatortype= locatortype.lower()
            bytype = self.getBytype(locatortype)
            waiting = WebDriverWait(self.driver, time)
            waiting.until(expected_conditions.presence_of_element_located((bytype, locator)))
            self.log.info("Waiting for presence of element with locator "+locator + " and locatortype "+locatortype)
        except:
            self.log.error("Waiting failed for presence of element with locator " + locator + " and locatortype " + locatortype)

    def waitforclickable(self, time, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            waiting = WebDriverWait(self.driver, time)
            bytype= self.getBytype(locatortype)
            element=waiting.until(expected_conditions.element_to_be_clickable((bytype, locator)))
            element.click()
            self.log.info("clicked after waiting for presence of element with locator " + locator + " and locatortype " + locatortype)
        except:
            self.log.error("not clicked after waiting for presence of element with locator " + locator + " and locatortype " + locatortype)

    def selectdropdownvaluebyvisibletext(self, locator, value, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            bytype = self.getBytype(locatortype)
            dropdown = Select(self.driver.find_element(bytype, locator))
            dropdown.select_by_visible_text(value)
            self.log.info("value "+ value + " selected in dropdown with locator "+locator +" and locatortype "+locatortype)
        except:
            self.log.error("value " + value + " not selected in dropdown with locator " + locator + " and locatortype " + locatortype)

    def clickradioonvalue(self, locator, value, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            elementlist = self.getelementlist(locator, locatortype)
            for element in elementlist:
                if element.get_attribute('value') == value:
                    element.click()
                    self.log.info("button with locator "+locator + " and locatortype "+locatortype +" and value "+value + " is clicked")
                else:
                    self.log.error("no element with value "+value + " found")
        except:
            self.log.error("Issue with clicking button with value "+value)

    def clickallradio(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            elementlist = self.getelementlist(locator, locatortype)
            for element in elementlist:
                element.click()
                time.sleep(2)
            self.log.info("All buttons with locator "+locator + " and locatortype " +locatortype + " clicked")
        except:
            self.log.error("All buttons with locator " + locator + " and locatortype " + locatortype + " not clicked")

    def validatepresence(self, locator, locatortype="id"):

            locatortype = locatortype.lower()
            elementlist = self.getelementlist(locator, locatortype)
            if len(elementlist) > 0:
                self.log.info("Element with locator "+locator + " and locatortype "+locatortype + " is present")
                return True
            else:
                self.log.info("Element with locator "+locator + " and locatortype "+locatortype + " is not present")
                return False

    def validateenabled(self, locator, locatortype = "id"):
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locator, locatortype)
            if element.is_enabled is True:
                self.log.info("Element with locator "+locator + " and locatortype "+locatortype + " is enabled")
                return True
            else:
                self.log.info("Element with locator "+locator + " and locatortype "+locatortype + " is not enabled")
                return False
        except:
            self.log.error("Issue with element while checking enabling of element")

    def webscroll(self, direction):

        direction = direction.lower()
        if direction == "up":
            self.driver.execute_script("window.scroll(0,-1000);")
            self.log.info("Scrolled up")
        elif direction == "down":
            self.driver.execute_script("window.scroll(0,1000);")
            self.log.info("Scroll down")

    def scrollinview(self, locator, locatortype):
        try:
            locatortype = locatortype.lower()

            element = self.getelement(locator, locatortype)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.log.info("Scrolled to element with locator "+locator + " and locatortype "+locatortype)
        except:
            self.log.error("Not scrolled to element with locator "+locator + " and locatortype "+locatortype)

    def getText(self, locator, locatortype = "id"):
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locator, locatortype)
            textmessage = element.text
            self.log.info("Text for element with locator "+locator + " and locatortype "+locatortype +" is"+textmessage)
            return textmessage
        except:
            self.log.error("No Text for element with locator " + locator + " and locatortype " + locatortype)

    def getScreenshot(self, resultmessage):

        filename = resultmessage + str(time.time()*1000)+ "png"
        ssdirectory = "../Screenshots/"
        relativefilename = ssdirectory + filename
        currentdirectory = os.path.dirname(__file__)
        destfilename = os.path.join(currentdirectory,relativefilename)
        destdirectory = os.path.join(currentdirectory, ssdirectory)

        try:
            if not os.path.exists(destdirectory):
                os.makedirs(destdirectory)
            self.driver.save_screenshot(destfilename)
            self.log.info("Screenshot saved")
        except:
            self.log.error("Screenshot not saved")

    def switch_frame(self, locator, locatortype):
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locator, locatortype)
            self.driver.switch_to.frame(element)
            self.log.info("switched to frame")
        except:
            self.log.error("not switched to frame")

    def switch_window(self, windownumber):
        try:
            self.driver.switch_to.window(self.driver.window_handles[windownumber])
            self.log.info("Switched to window number "+windownumber)
        except:
            self.log.error("Window switch failed")

    def switch_alert(self):
        try:
            alertm=self.driver.switch_to.alert
            self.log.info("Switched to alert")
            return alertm
        except:
            self.log.error("Not switched to alert")
