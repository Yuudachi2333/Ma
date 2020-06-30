# from PIL import Image
# from selenium import webdriver
# import time
# from mylesson.work.ShowapiRequest import ShowapiRequest
# import pytesseract
# # pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# # image = Image.open('D:\\report\\uwv6.jpg')
# # code= pytesseract.image_to_string(image)
# # print(code)
#
#
# driver = webdriver.Chrome()
# driver.get('http://www.5itest.cn/register')
# # code_element = driver.find_element_by_id('checkImg')
# code_element = driver.find_element_by_id('getcode_num')
# left = code_element.location['x']
# top = code_element.location['y']
# right = code_element.size['width'] + left
# height = code_element.size['height'] + top
# #
# filepath = time.strftime('%Y%m%d%H%M%S')
# filename = 'D:\\report\\'+ filepath + '.png'
# driver.save_screenshot(filename)
# im = Image.open(filename)
# img = im.crop((left, top, right, height))
# img.save(filename)
# #
# # time.sleep(1)
# # code_image = Image.open(filename)
# # code= pytesseract.image_to_string(code_image)
# # print(code)
# #
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/example.html')
# e = WebDriverWait(driver,10).until(EC.invisibility_of_element_located(driver.find_element_by_id("register_email")))
# e.sendkey("123")


wait = WebDriverWait(driver,10)
wait.until(EC.title_is('selenium处理基本页面元素'),'页面超时')
alert = driver.find_element_by_name('alterbutton').click()
try:
    wait.until(EC.alert_is_present())
    print('alert元素')
except:
    print("没有alert")