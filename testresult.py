from calculator import Calculate
import unittest
import HTMLTestRunner

class TestResult(unittest.TestCase):
    def setUp(self):
        print("testing start!")

    def testAdd(self):
        i = Calculate(5,6)
        i = i.add()
        self.assertIsInstance(i, float)

    def testReduce(self):
        j = Calculate(19, 11)
        j = j.reduce()
        self.assertEqual(j, 9, msg='没减对啊！')

    def tearDown(self):
        print("well done!")
if __name__ == "__main__":
suit1 = unittest.TestSuite()
    suit1.addTest(TestResult("testAdd"))
    suit2 = unittest.TestSuite()
    suit2.addTest(TestResult("testReduce"))
    suit2.addTest(TestResult("testAdd"))
    result = open("d:\\test.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=result, title=u"测试报告", description=u"测试执行情况")
    runner.run(suit2)
    result.close()
