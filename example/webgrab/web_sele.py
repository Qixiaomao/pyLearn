# -*- coding:utf-8 -*-


#C:\Python27\geckodriver-v0.26.0-win64\geckodriver.exe
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")
'''assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
'''
#driver.close()


