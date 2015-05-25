#coding:utf-8
"""
This module is:
- Message Box Module
- entrance : under "Message" Tab
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


class MessageBox(unittest.TestCase):
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

    #回复评论
    def test_002_ReplyComment(self):
        box = config.driver.find_elements_by_css_selector('a.item.box-col')
        print len(box)#4
        #点击 消息
        box[1].click()
        print "点击 消息"

        lists = config.driver.find_elements_by_css_selector('a.box-col.item-list')
        print len(lists)#14
        lists[1].click()
        print "点击 评论"

        buttons = config.driver.find_elements_by_css_selector('button.btn.btn-normal.btn-replay')
        print "回复按钮有" + str(len(buttons)) + "个" #10
        index = random.choice(range(len(buttons)))
        buttons[index].click()
        print "评论第" + str(index + 1) + "条微博"
        config.driver.find_element_by_id('txt-publisher').send_keys("good~")
        config.driver.find_element_by_css_selector('a.fr.txt-link').click()
        print "评论成功"
        time.sleep(2)
        config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
        print "返回"

    #删除评论
    #删除评论箱中我的任何一条评论
    def test_003_DeleteComment(self):
        lists = config.driver.find_elements_by_css_selector('a.box-col.item-list')
        print len(lists)#14
        lists[1].click()
        print "点击 评论"
        config.driver.find_element_by_css_selector('i.icon-font.icon-font-arrow-down').click()
        config.driver.find_element_by_xpath('//*[@id="J-scroll"]/a[3]').click()
        print "点击 下拉菜单中 我发出的"
        comments = config.driver.find_elements_by_css_selector('p.default-content.txt-xl')
        print len(comments)
        index = random.choice(range(len(comments)))
        print "删除第" + str(index + 1) + "条微博"
        comments[index].click()
        time.sleep(2)
        config.driver.find_element_by_xpath('/html/body/div[2]/div/section/a[2]').click()
        # config.driver.find_element_by_css_selector('div.box-col.item-list').click()
        print "点击 弹层里的删除"
        time.sleep(3)
        alert = config.driver.switch_to.alert
        assert '确定要删除这条微博' in alert.text
        alert.accept()
        time.sleep(2)
        config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
        print "返回"


    #删除私信-清空对话
    def test_004_DeleteDialogue(self):
        time.sleep(3)
        lists = config.driver.find_elements_by_css_selector('a.box-col.item-list')
        print len(lists)#14,有时9
        index = random.choice(range(4,len(lists)))
        print index
        lists[index].click()
        print "点击与某人的对话"
        config.driver.find_element_by_css_selector('a.more-sub-header.right').click()
        time.sleep(2)
        # config.driver.find_element_by_css_selector('a.clearit').click()
        config.driver.find_element_by_xpath('//*[@id="popLayer"]/div/div[2]/a[2]').click()
        print "点击 清空对话"
        time.sleep(3)
        alert = config.driver.switch_to.alert
        assert '确认清空' in alert.text
        alert.accept()
        time.sleep(2)
        config.driver.find_element_by_css_selector('a.back-header.left.chat_back.clean_all').click()
        print "返回"


    #刷新
    def refresh(self):
         # config.driver.find_element_by_name('加载中')
         refresh = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_refresh')
         print type(refresh)
         refresh.click()
         time.sleep(3)
         print "点击刷新按钮"


#---START OF SCRIPT
#执行的入口
if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(MessageBox)#根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    # unittest.TextTestRunner(verbosity=2).run(suite)
    suit = unittest.TestSuite()#定义一个单元测试容器
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(MessageBox))#将测试用例加入到容器中
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    abspath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'html_result'))
    filename = abspath + "/MessageBox_" + now + ".html" #定义报告存放路径，支持相对路径
    print filename
    fp= file(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='H5主功能_消息箱_测试报告',
        description='Report Descriptions'
    )
    #自动进行测试
    runner.run(suit)


