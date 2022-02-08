from selenium import webdriver
from time import sleep

from resources.secrets import username, password

class JayBot():
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get('https://tinder.com')
		sleep(2)
	
	def log_on(self):
		logon_button = self.driver.find_element_by_xpath('//*[@id="q1413092675"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
		logon_button.click()

		sleep(2)
		
		logon_with_phone = self.driver.find_element_by_xpath('//*[@id="q-315288401"]/div/div/div[1]/div/div[3]/span/div[3]/button')
		logon_with_phone.click()


def main():
	jay = JayBot()
	jay.log_on()
