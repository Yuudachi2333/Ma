from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver.get('https://www.baidu.com/')
# driver.maximize_window()
# driver.get('http://news.baidu.com/')
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()

# eml = driver.find_element_by_id("kw")
# eml.send_keys("selenium")
# print(driver.find_element_by_id("kw").size)
# driver.find_element_by_id("kw").send_keys("NBA")
# driver.find_element_by_id('kw').clear()
# driver.find_element_by_id("kw").send_keys("test")
# text = driver.find_element_by_partial_link_text("地图").text
# # link = driver.find_element_by_link_text("新闻").get_attribute("href")
# # print(link)
# # print(text)
# # # driver.find_element_by_xpath("//input[contains(@value,'百度一下')]").click()
# # time.sleep(2)
# # # driver.find_element_by_partial_link_text("NBA中国数字媒体独家官方合作伙伴").click()
# # # driver.find_element_by_xpath("(//a[contains(@target,'_blank')])[106]").click()
# # time.sleep(2)
# # driver.quit()
# e1 = driver.find_element_by_id("su")
# ActionChains(driver).context_click(e1).perform()
# time.sleep(2)
# e2 = driver.find_elements_by_name("tj_settingicon")[1]
# ActionChains(driver).move_to_element(e2).perform()
# time.sleep(2)
# driver.quit()


# driver.get('https://map.baidu.com/')
# driver.find_element_by_id("sole-input").send_keys("天府广场")
# driver.find_element_by_id("search-button").click()
# time.sleep(3)
# driver.find_elements_by_class_name("n-blue")[0].click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="route-go"]/span[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("天府三街")
# time.sleep(2)
# driver.find_element_by_id("search-button").click()
# time.sleep(2)
# e1 = driver.find_element_by_xpath('//*[@id="RA_ResItem_0"]/table/tbody/tr[1]/td[1]/a')
# ActionChains(driver).move_to_element(e1)
# ActionChains.move_by_offset()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="RA_ResItem_0"]/table/tbody/tr[1]/td[2]/div').click()
#
#
# time.sleep(5)
# driver.quit()

driver.get('https://www.baidu.com/')
driver.find_element_by_id("kw").send_keys("NBA123456")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
for i in range (len("NBA123456")):
    driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
driver.find_element_by_id('su').click()
print(driver.title)
print(driver.current_url)

time.sleep(2)
for i in range(5):
    driver.find_element_by_tag_name("html").send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
for i in range(5):
    driver.find_element_by_tag_name("html").send_keys(Keys.ARROW_UP)
    time.sleep(1)
for i in range(5):
    driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(5):
    driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)
    time.sleep(1)

print(driver.page_source)
driver.quit()

