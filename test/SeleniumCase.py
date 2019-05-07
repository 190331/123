from selenium import webdriver

window = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
window.get("http://www.nzhg.co.nz/")
window.find_element_by_class_name("close").click()