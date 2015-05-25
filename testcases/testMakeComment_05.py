#coding:utf-8
"""
This Module is:
-Make Comment Module
-注意点:要注意到异常情况,评论失败的处理
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


class MakeComment(unittest.TestCase):
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

    #发布评论
    def test_002_MakeComment(self):
       box = config.driver.find_elements_by_css_selector('a.item.box-col')
       print len(box)#4
       #点击 首页
       box[0].click()
       print "点击 首页"
       time.sleep(2)
       box = config.driver.find_elements_by_css_selector('a.box-col.txt-s')
       tmpList = []
       for i in range(1, len(box) / 3):
         tmpList.append(i * 3 - 2)
       index = random.choice(tmpList)
       print index
       print "评论的第", (index + 2) / 3 ,"条微博~"
       comment = box[index]
       comment.click()
       print "点击评论按钮"
       time.sleep(2)
       #输入评论
       # start = time.time()  #timestamp
       start = datetime.now()
       print start
       if config.driver.find_elements_by_css_selector('a.box-col.txt-s'):
           box = config.driver.find_elements_by_css_selector('a.box-col.txt-s')
           print "len:", len(box) #3
           box[1].click()
           print "已有评论的情况~"
           config.driver.find_element_by_id('txt-publisher').send_keys('Thumb Up~')
           end = datetime.now()
           print end
           print 'Waiting Time: %s' % (end - start)
           config.driver.find_element_by_css_selector('a.fr.txt-link').click()
           #返回
           time.sleep(2)
           try:
              config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
              print "发送评论成功"
           except:
               print "发送评论失败" #only author's attention user can make comment.
               buttons = config.driver.find_elements_by_css_selector('a.fl.txt-link')
               buttons[0].click()
               print "点击取消"
               time.sleep(2)
       else:
           print "还没有评论的情况~"
           config.driver.find_element_by_id('txt-publisher').send_keys('make some comment~')
           end = datetime.now()
           print end
           print 'Waiting Time: %s' % (end - start)
           config.driver.find_element_by_css_selector('a.fr.txt-link').click()
           #还需要处理异常情况,only author's attention user can make comment.
           # do something

       time.sleep(2)
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
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(MakeComment))#将测试用例加入到容器中
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    abspath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'html_result'))
    filename = abspath + "/MakeComment_" + now + ".html" #定义报告存放路径，支持相对路径
    print filename
    fp= file(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='H5主功能_评论模块_测试报告',
        description='Report Descriptions'
    )
    #自动进行测试
    runner.run(suit)

