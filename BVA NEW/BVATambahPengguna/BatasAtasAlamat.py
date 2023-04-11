# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BatasAtasAlamat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_batas_atas_alamat(self):
        driver = self.driver
        driver.get("https://sas-kia-deploy.vercel.app/dashboard/user")
        driver.find_element_by_link_text("Tambah Pengguna").click()
        driver.find_element_by_id("mui-7").click()
        driver.find_element_by_id("mui-7").clear()
        driver.find_element_by_id("mui-7").send_keys("Alamatalamatalamatalamatalamatalamatalamatalamatalamatalamatalamatalamatalamatalamatalamatalamatal123")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/span").click()
    
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
