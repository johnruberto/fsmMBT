from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()


# go to the google home page
driver.get("http://blog.ruberto.com")

customers_link = driver.find_element_by_class_name("tag-link-9")
customers_link.click()
print driver.title

management_link = driver.find_element_by_class_name("tag-link-12")
management_link.click()
print driver.title

testauto_link = driver.find_element_by_class_name("tag-link-3")
testauto_link.click()
print driver.title


