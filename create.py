import sys
import os
from selenium import webdriver

path = "/Users/uyentran/Desktop/Admin/MyProjects/"
driverLocation = '/Users/uyentran/Desktop/Admin/MyProjects/chromedriver'
browser = webdriver.Chrome(driverLocation)
browser.get('http://github.com/login')

def create():
	folderName = str(sys.argv[1])
	os.makedirs(path + folderName)
	python_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
	python_button.send_keys('uyentrannn')
	python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
	python_button.send_keys('babyZ4ever')
	python_button = browser.find_elements_by_xpath("//*[@id='login']/form/div[4]/input[9]")[0]
	python_button.click()
	browser.get('http://github.com/new')
	python_button = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
	python_button.send_keys(folderName)
	python_button = browser.find_element_by_css_selector('button.first-in-line')
	python_button.submit()
	browser.quit()

if __name__ == "__main__":
	create()   
