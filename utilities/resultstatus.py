from base.selenium_base import Selenium_base
import utilities.custom_logging as cl
import logging


class ResultStatus(Selenium_base):
    resultlist = []
    log = cl.log(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.resultlist = []

    def results(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("Pass")
                    self.log.info(resultmessage + " working fine")
                else:
                    self.resultlist.append("Fail")
                    self.log.error(resultmessage+ " not working fine")
            else:
                self.resultlist.append("Fail")
                self.log.error(resultmessage+ " not working fine")
        except:
            self.log.error(resultmessage+ " not working fine")

    def marktest(self, result, resultmessage):
        self.results(result, resultmessage)

    def marltestfinal(self, result, resultmessage, tcname):
        self.results(result, resultmessage)

        if "Fail" in self.resultlist:
            self.resultlist.clear()
            self.log.error("########## " +tcname + "failed")
            assert True == False
        else:
            self.resultlist.clear()
            self.log.info("########## "+ tcname + "passed")
            assert True == True
