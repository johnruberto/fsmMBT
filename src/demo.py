#demo.py, automatically generated webdriver code
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://blog.ruberto.com")
link = driver.find_element_by_class_name( "tag-link-3" )
link.click()
assert driver.title == "Test Automation"
print "Expected: Test Automation Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-9" )
link.click()
assert driver.title == "Customers"
print "Expected: Customers Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-3" )
link.click()
assert driver.title == "Test Automation"
print "Expected: Test Automation Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-12" )
link.click()
assert driver.title == "Management"
print "Expected: Management Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-3" )
link.click()
assert driver.title == "Test Automation"
print "Expected: Test Automation Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-3" )
link.click()
assert driver.title == "Test Automation"
print "Expected: Test Automation Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-3" )
link.click()
assert driver.title == "Test Automation"
print "Expected: Test Automation Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-12" )
link.click()
assert driver.title == "Management"
print "Expected: Management Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-3" )
link.click()
assert driver.title == "Test Automation"
print "Expected: Test Automation Got: ",driver.title
link = driver.find_element_by_class_name( "tag-link-9" )
link.click()
assert driver.title == "Customers"
print "Expected: Customers Got: ",driver.title
driver.quit()
print "So long, and thanks for all the fish"