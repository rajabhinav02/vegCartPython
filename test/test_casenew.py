import pytest

from page.MenuPage import Menu

from utilities.resultstatus import ResultStatus


@pytest.mark.usefixtures("setup")
class TestVegCart:

    @pytest.fixture(autouse=True)
    def classsetup(self):
        self.mn = Menu(self.driver)
        self.rs = ResultStatus(self.driver)

    #@pytest.mark.usefixtures("testfruit")
    def test_fruitorder(self, testfruit):
        self.driver.implicitly_wait(3)
        self.mn.submitFruits(testfruit['FruitName'])
        listvalidationone = self.mn.validateitemsselected()
        self.rs.marktest(listvalidationone, "first page list failing")
        self.ord= self.mn.clickfirstcheckout()

        am= self.ord.validateamount()
        self.rs.marktest(am, "Amount in table with quantity and price")
        tot=self.ord.validatetotalselected()
        self.rs.marktest(tot, "Both the total amounts")
        disc= self.ord.validatecouponapplied(testfruit["CouponCode"], testfruit["WaitTime"])
        self.rs.marktest(disc, "Discount check")
        self.cn= self.ord.PlaceOrderf()
        self.cn.submittransaction(testfruit["Country"])
        fi=self.cn.validateconfirmation()
        self.rs.marltestfinal(fi, "Final submission", "test_fruitorder")
