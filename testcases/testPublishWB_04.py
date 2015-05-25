#coding:utf-8
"""
This Module is:
-Publish Weibo Module
"""

import os
import unittest
import time
import random
from datetime import datetime
import config
import functions
import HTMLTestRunner

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class PublishWBModule(unittest.TestCase):
    "Class to run tests against the chrome browser"
    def setUp(self):
        "Setup for the test"
        pass

    def tearDown(self):
       "Tear down the test"
       # self.config.driver.quit()#执行完后退出应用
       pass

    #登录操作
    def test_001_Login(self):
        try:
            config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
            print "已登录~"
        except:
            print "立即登录"
            functions.login()
            print "登录完成~"
        finally:
            print "pass~"

    #发布微博-包含英文
    def test_002_PublishWbEng(self):
        box = config.driver.find_elements_by_css_selector('a.item.box-col')
        print len(box)#4
        #点击 首页
        box[0].click()
        print "点击 首页"
        time.sleep(2)
        publish = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
        publish.click()

        content = config.driver.find_element_by_id("txt-publisher")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
        num = random.randint(1,100)
        content.send_keys("It's a beautiful day" + str(num) +" " + now + "~")
        config.driver.find_element_by_css_selector('a.fr.txt-link').click()
        print "发微博成功~"
        time.sleep(5)
        self.refresh()

    # 发微博@某人
    def test_003_AtSomeone(self):
        publish = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
        publish.click()

        content = config.driver.find_element_by_id("txt-publisher")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
        num = random.randint(1,100)
        content.send_keys("@2013wltest_002 holiday" + str(num) +" " + now + "~")
        config.driver.find_element_by_css_selector('a.fr.txt-link').click()
        print "@某人成功~"
        time.sleep(3)
        self.refresh()

    #发布微博-内容：包含中文
    def test_004_PublishWbZH(self):
        publish = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
        publish.click()

        content = config.driver.find_element_by_id("txt-publisher")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
        num = random.randint(1,100)
        content.send_keys(u'今儿是个好日子啊~' + str(num) +" " + now + "~")

        config.driver.find_element_by_css_selector('a.fr.txt-link').click()
        print "发微博成功~"
        time.sleep(5)
        self.refresh()

    #发布微博-内容：包含链接
    def test_005_PublishWbURL(self):
        publish = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
        publish.click()

        content = config.driver.find_element_by_id("txt-publisher")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
        num = random.randint(1,100)
        content.send_keys("http://www.baidu.com" +" " + now + "~")

        config.driver.find_element_by_css_selector('a.fr.txt-link').click()
        print "发微博成功~"
        time.sleep(5)
        self.refresh()



    #刷新
    def refresh(self):
         # config.driver.find_element_by_name('加载中')
         refresh = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_refresh')
         print type(refresh)
         refresh.click()
         time.sleep(3)
         print "点击刷新按钮"


#---START OF SCRIPT
if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(ProfileModule)#根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    # unittest.TextTestRunner(verbosity=2).run(suite)
    suit = unittest.TestSuite()#定义一个单元测试容器
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(PublishWBModule))#将测试用例加入到容器中
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    abspath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'html_result'))
    filename = abspath + "/PublishWB_" + now + ".html" #定义报告存放路径，支持相对路径
    print filename
    fp= file(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='H5主功能_发微博_测试报告',
        description='Report Descriptions'
    )
    #自动进行测试
    runner.run(suit)


