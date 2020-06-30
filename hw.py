from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from calculator import Calculate
import unittest
'''
现有一个登陆页面，页面中包含用户名和密码两个输入框，一个登陆按钮，
现要求使用unittest对该页面进行自动化测试脚本设计
url ： http://192.168.0.134:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php
其中用户名输入框name=username，密码输入框name=password，登陆按钮name=submit
'''


driver = webdriver.Chrome()
driver.get('http://192.168.0.134:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php')
time.sleep(5)
driver.find_element_by_name('username').send_keys('username')
time.sleep(5)
driver.find_element_by_name('password').send_keys('password')
time.sleep(5)
driver.find_element_by_class_name('submit').click()
time.sleep(5)
driver.quit()
