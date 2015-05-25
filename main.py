#coding:utf-8

import unittest, time, re
import os
import HTMLTestRunner
from datetime import datetime

from testProfileModule_01 import ProfileModule
from testMeModule_02 import MeModule
from testMessageBox_03 import MessageBox
from testPublishWB_04 import PublishWBModule

def run_suit():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    abspath = os.path.abspath(os.path.join(os.path.dirname(__file__),'html_result'))
    filename = abspath + "/report_" + now + ".html" #定义报告存放路径，支持相对路径
    print filename
    fp= file(filename, "wb")
    suit = unittest.TestSuite()
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ProfileModule))
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(MeModule))
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(MessageBox))
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(PublishWBModule))

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="Android Chrome Browser Test Report",
        description=" Test Cases"
    )
    runner.run(suit)

run_suit()