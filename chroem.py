from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from calculator import Calculate
# import unittest
'''
现有一个登陆页面，页面中包含用户名和密码两个输入框，一个登陆按钮，
现要求使用unittest对该页面进行自动化测试脚本设计
url ： http://192.168.0.134:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php
其中用户名输入框name=username，密码输入框name=password，登陆按钮name=submit
'''


driver = webdriver.Chrome()
driver.get('http://192.168.0.134:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php')
time.sleep(5)
driver.get('https://search.bilibili.com/?spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.10')
driver.find_element_by_id('search-keyword').send_keys('奥利给')
time.sleep(5)
driver.find_element_by_class_name('searchBtn').click()
time.sleep(5)
driver.quit()
driver.get('https://bbs.nga.cn/thread.php?fid=-7202235')
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.quit()


# driver = webdriver.Chrome()
# driver.get('https://map.baidu.com/@11588633,3555881,13z')
# time.sleep(5)
# driver.find_element_by_id('sole-input').send_keys('火车站')
# time.sleep(5)
# driver.find_element_by_id('search-button').click()
# time.sleep(5)
# driver.find_element_by_class_name('row').click()
# time.sleep(5)
# driver.find_element_by_id('route-go').click()
# time.sleep(5)e
# driver.quit()

# driver = webdriver.Chrome()
# driver.get('https://bbs.nga.cn/thread.php?stid=20775037')
# time.sleep(5)
# driver.find_element_by_class_name('silver').send_keys(Keys.CONTROL,'a')
# time.sleep(5)
# driver.find_element_by_id('postcontent0').send_keys(Keys.CONTROL,'c')
# time.sleep(5)
# driver.find_element_by_id('unisearchinput').send_keys(Keys.CONTROL,'v')
# time.sleep(5)
# driver.find_element_by_id('unisearchinput').send_keys(Keys.ENTER)
# time.sleep(5)

driver = webdriver.Chrome()
driver.get('https://tieba.baidu.com/index.html')
time.sleep(5)
driver.find_element_by_xpath("//a[@rel='noreferrer'][contains(.,'登录')]").click()
time.sleep(5)
# driver.switch_to_frame('na')
driver.find_element_by_xpath("//p[@class='tang-pass-footerBarULogin pass-link'][contains(@id,'footerULoginBtn')][contains(.,'用户名登录')]").click()
time.sleep(5)
driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys('Marcbin2333')
time.sleep(5)
driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('mipu97820',Keys.ENTER)
time.sleep(5)
driver.quit()






