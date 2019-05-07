# coding = utf-8

from selenium import webdriver
#导包
browser = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
#创建对象且赋值控制Chrome浏览器后面参数跟Chrome安装路径
browser.get("http://www.baidu.com/")
#打开浏览器后面参数跟网址
browser.find_element_by_id("kw").send_keys("selenium")
#百度输入框id为“kw”且输入selenium
browser.find_element_by_id("su").click()
#百度搜索button的id为su 且点击
print(browser.title)
#输出浏览器title


browser.fin