import unittest
from Math import Count
class Test(unittest.TestCase):
    def start(self):
        print('start')
    def tearDown(self):
        print('end')
    def test_login_succes(self):
        print('succes')
    def test_login_fail(self):
        print('fail')


    def test_add(self):
        test = Count(6,6)
        self.assertAlmostEqual(test.add(),12,"用例失败")


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test('test_add'))
    runner = unittest.TextTestRunner()
    runner.run(suite)