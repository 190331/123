#-*- coding: UTF-8 -*-
#__author__ = 'LANG'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
def login():
    username = driver.find_element_by_name("userName")
    username.send_keys("15712990664")
    password = driver.find_element_by_id("password")
    password.send_keys("langshuo12")
    login = driver.find_element_by_class_name("ant-btn-lg")
    login.click()
def logout():
    driver.maximize_window()
    time.sleep(10)
    nickname = driver.find_element_by_class_name("ant-avatar-circle")
    print("nickname的元素是"+str(nickname))
    nickname.click()
    time.sleep(10)
    logout=driver.find_element_by_class_name("anticon-logout")
    print("退出登录的元素是"+str(logout))
    time.sleep(5)
    logout.click()

driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.get("http://ltj.nz/order/list")


login()
logout()