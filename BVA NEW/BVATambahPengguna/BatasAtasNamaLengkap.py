# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BatasAtasNamaLengkap(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_batas_atas_nama_lengkap(self):
        driver = self.driver
        driver.get("https://sas-kia-deploy.vercel.app/landing-page")
        driver.find_element_by_xpath("//div[@id='root']/div/header/div/div[2]/ul/li[5]/a/span").click()
        driver.get("https://sas-kia-deploy.vercel.app/Login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("agoes.soetanto2@gmail.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("5@AGOES67s")
        driver.find_element_by_id("mui-1").click()
        self.assertEqual("Login Sukses!", self.close_alert_and_get_its_text())
        driver.get("https://sas-kia-deploy.vercel.app/landing-page")
        driver.find_element_by_xpath("//div[@id='root']/div/header/div/div[2]/ul/li[5]/a/span").click()
        driver.get("https://sas-kia-deploy.vercel.app/dashboard/app")
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/ul/a[2]/div[2]").click()
        driver.get("https://sas-kia-deploy.vercel.app/dashboard/user")
        driver.find_element_by_link_text("Tambah Pengguna").click()
        driver.find_element_by_xpath("//html/body/div[2]/div[3]/div/div/p/div/div[1]/div[1]/div/input").click()
        driver.find_element_by_xpath("//html/body/div[2]/div[3]/div/div/p/div/div[1]/div[1]/div/input").clear()
        driver.find_element_by_xpath("//html/body/div[2]/div[3]/div/div/p/div/div[1]/div[1]/div/input").send_keys("Namalengkapnamalengkapnamalengkapnamalengkapnamaley")
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
