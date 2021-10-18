import logging
import time

from base.selenium_base import Selenium_base
from page.OrderPage import OrderP
from utilities import custom_logging as cl


class Menu(Selenium_base):
    log = cl.log(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    searchbox = "//input[@type='search' and contains(@placeholder, 'Search')]"
    searchbutton = ".search-button"
    addbutton = "//button[text()= 'ADD TO CART']"
    itemname = "parent::div/parent::div//h4"
    bag = "img[alt='Cart']"
    afterselectionproduct= "//li[@class='cart-item']//p[@class='product-name']"
    proceedcheckout = "//button[contains(text(), 'PROCEED')]"
    listone = []
    listtwo = []

    def sendfruitname(self, fruitname):
        self.senddata(fruitname, self.searchbox, "xpath")

    def clicksearch(self):
        self.clickelement(self.searchbutton, "css")

    def clickaddbutton(self):
        buttons = self.getelementlist(self.addbutton, "xpath")
        for button in buttons:
            time.sleep(3)
            name = self.getxpathfromchild(button,self.itemname).text
            #name= button.find_element_by_xpath("parent::div/parent::div//h4").text
            #lname = name.text
            time.sleep(2)
            self.listone.append(name)
            time.sleep(2)
            button.click()
            time.sleep(3)

    def clickselectfinal(self):
        self.clickelement(self.bag,"css")

    def getselecteditemlist(self):
        names = self.getelementlist(self.afterselectionproduct, "xpath")
        for name in names:
            self.listtwo.append(name)

    def clickfirstcheckout(self):
        self.clickelement(self.proceedcheckout, "xpath")
        ord = OrderP(self.driver)
        return ord

    def validateitemsselected(self):
        self.log.info(self.listone, self.listtwo)
        if self.listone == self.listtwo:
            return True
        else:
            return False


    def submitFruits(self, fruitname):
        self.sendfruitname(fruitname)
        self.clicksearch()
        self.clickaddbutton()
        self.clickselectfinal()
        self.getselecteditemlist()
        # ord = self.clickfirstcheckout()
        # return ord


