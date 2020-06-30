import unittest
from selenium import webdriver
import HTMLTestRunner

class Test(unittest.TestCase):


    def setUp(self):
        self.driver =  webdriver.Chrome()
        self.driver.get('http://192.168.0.134:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php')

    def tearDown(self):
        self.driver.quit()

    def test_login_succes(self):
        '''
        caseid 1 ：验证用户名密码正确登录成功
        :return:
        '''
        self.driver.find_element_by_name("username").send_keys("test13")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name('submit').click()
        self.driver.save_screenshot(r"D:\study\webautotest\images\loginsuccess.png")
        self.assertIn("欢迎您回来！",self.driver.page_source,"用例失败")

    def test_login_fail(self):
        '''
        caseid 2 :验证用密码错误登录失败
        :return:
        '''
        self.driver.find_element_by_name("username").send_keys("test13")
        self.driver.find_element_by_name("password").send_keys("1234566")
        self.driver.find_element_by_name('submit').click()
        self.driver.save_screenshot(r"D:\study\webautotest\images\loginfail.png")
        self.assertNotIn("欢迎您回来！", self.driver.page_source, "用例失败")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest((Test("test_login_succes")))
    suite.addTest((Test("test_login_fail")))
    # suite.addTests(map(Test, ['test_sheng', 'test_login_fail']))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    result=open("d:\\test.html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=result,title=u"测试报告",description=u"测试执行情况")
    runner.run(suite)
    result.close()


