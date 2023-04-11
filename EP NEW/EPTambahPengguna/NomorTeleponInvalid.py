# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NomorTeleponInvalid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_nomor_telepon_invalid(self):
        driver = self.driver
        driver.get("https://sas-kia-deploy.vercel.app/dashboard/user")
        driver.find_element_by_link_text("Tambah Pengguna").click()
        driver.find_element_by_id("mui-5").click()
        driver.find_element_by_id("mui-5").clear()
        driver.find_element_by_id("mui-5").send_keys("alvin soetanto")
        driver.find_element_by_id("mui-6").click()
        driver.find_element_by_id("mui-6").clear()
        driver.find_element_by_id("mui-6").send_keys("alvinsoetanto@gmail.com")
        driver.find_element_by_id("mui-7").click()
        driver.find_element_by_id("mui-7").clear()
        driver.find_element_by_id("mui-7").send_keys("Babat, Lamongan")
        driver.find_element_by_id("mui-8").click()
        driver.find_element_by_id("mui-8").clear()
        driver.find_element_by_id("mui-8").send_keys("351167321367921704")
        driver.find_element_by_id("mui-9").click()
        driver.find_element_by_id("mui-9").clear()
        driver.find_element_by_id("mui-9").send_keys("&%$#$iI")
        driver.find_element_by_xpath("//html/body/div[2]/div[3]/div/div/p/div/div[5]/div/div").click()
        driver.find_element_by_xpath("//html/body/div[3]/div[3]/ul/li[1]").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.save_screenshot('.png')
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
