import logging

from base.selenium_base import Selenium_base
from page.ConfirmPage import Confirm
import utilities.custom_logging as cl


class OrderP(Selenium_base):
    log = cl.log(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    brandselected= ".product-name"
    quantityselected= ".quantity"
    price = "//table/tbody/tr/td[4]/p"
    stotal = "//table/tbody/tr/td[5]/p"
    codetextbox = ".promocode"
    applybutton = ".promoBtn"
    totaldisplayed = ".totAmt"
    discountamt = ".discountAmt"
    codeconfirmation = ".promoInfo"
    List3 = []
    PlaceOrder = "//button[text()='Place Order']"


    def getProductName(self):
        pnames = self.getelementlist(self.brandselected, "css")
        for pname in pnames:
            self.List3.append(pname)

    def validateamount(self):
        quantities = self.getelementlist(self.quantityselected, "css")
        prices = self.getelementlist(self.price, "xpath")
        totals = self.getelementlist(self.stotal, "xpath")

        for quantity in quantities:
            for price in prices:
                for total in totals:
                    if int(quantity.text)* int(price.text) == int(total.text):
                        return True
                    else:
                        return False

    def getselectedTotal(self):
        selectedtotals = self.getelementlist(self.stotal,"xpath")
        sum = 0
        for seltot in selectedtotals:
            seltota = int(seltot.text)
            sum = sum+ seltota
        return sum

    def sendcoupon(self, coupon):
        self.senddata(coupon, self.codetextbox, "css")
        self.clickelement(self.applybutton, "css")

    def validatetotalselected(self):
        selectedtotal=self.getText(self.totaldisplayed)
        sumtotal = self.getselectedTotal()
        if int(selectedtotal)==int(sumtotal):
            return True
        else:
            return False

    def waitforcodeapply(self, time):
        self.waitforpresence(time, self.codeconfirmation, "css")

    def validatecouponapplied(self,coupon, time):
        self.sendcoupon(coupon)
        self.waitforcodeapply(time)
        afterdiscount= self.getText(self.discountamt, "css")
        totalselecteddis = self.getText(self.totaldisplayed, "css")
        if int(totalselecteddis) > float(afterdiscount):
            return True
        else:
            return False

    def PlaceOrderf(self):
        self.clickelement(self.PlaceOrder, "xpath")
        cn = Confirm(self.driver)
        return cn

    def submitorder(self):
        cn=self.PlaceOrderf()