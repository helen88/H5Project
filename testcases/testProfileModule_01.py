#coding:utf-8
"""
This Module is:
-Profile Module
-entrance: under "Profile" Tab
"""

import os
import unittest
import time
import random
from datetime import datetime
import config
import HTMLTestRunner

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ProfileModule(unittest.TestCase):
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
        print "chrome上下文: "
        contexts = config.driver.contexts
        for cotext in contexts:
            print cotext   #output: NATIVE_APP , WEBVIEW_1

        config.driver.get("http://m.weibo.cn")
        config.driver.implicitly_wait(30)
        print "跳转到微博登陆页"

        loginBtn = config.driver.find_element_by_css_selector('a.btn.btnWhite')
        print type(loginBtn)
        loginBtn.click()
        config.driver.implicitly_wait(30)
        time.sleep(3)

        username = config.driver.find_element_by_id('loginName')
        username.clear()
        username.send_keys("wlsec_004@sina.com")
        psw = config.driver.find_element_by_id('loginPassword')
        psw.send_keys('1qaz2wsx')
        #点击登录按钮
        config.driver.find_element_by_id('loginAction').click()
        print "登录成功"
        time.sleep(3)
        try:
            # config.driver.context('NATIVE_APP')   Not OK~
            config.driver.switch_to.context('NATIVE_APP')
            print "转换 context"
            config.driver.find_element_by_id('com.android.chrome:id/infobar_close_button').click()
            print "关闭提示保存密码弹窗~"
            config.driver.switch_to.context('WEBVIEW_1')
        except:
            print "没有弹窗"

    # #发布微博
    # def test_002_PublishWB(self):
    #     publish = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
    #     publish.click()
    #
    #     content = config.driver.find_element_by_id("txt-publisher")
    #     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
    #     num = random.randint(1,100)
    #     content.send_keys("It's a beautiful day" + str(num) +" " + now + "~")
    #     config.driver.find_element_by_css_selector('a.fr.txt-link').click()
    #     print "发微博成功~"
    #     time.sleep(5)
    #     self.refresh()
    #
    # # 发微博@某人
    # def test_003_Refer2me(self):
    #     publish = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
    #     publish.click()
    #
    #     content = config.driver.find_element_by_id("txt-publisher")
    #     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
    #     num = random.randint(1,100)
    #     content.send_keys("@2013wltest_002 holiday" + str(num) +" " + now + "~")
    #     config.driver.find_element_by_css_selector('a.fr.txt-link').click()
    #     print "@某人成功~"
    #     time.sleep(3)
    #     self.refresh()
    #
    # #发布微博-仅对自己可见-内容：包含中文
    # def test_004_PublishWB(self):
    #     publish = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
    #     publish.click()
    #
    #     content = config.driver.find_element_by_id("txt-publisher")
    #     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
    #     num = random.randint(1,100)
    #     content.send_keys(u'加油' + str(num) +" " + now + "~")
    #     #设置仅对自己可见
    #     # for i in range(2):
    #     #     config.driver.find_element_by_css_selector('a.icon_wbtype.fr').click()
    #     #     time.sleep(1)
    #     #
    #     config.driver.find_element_by_css_selector('a.fr.txt-link').click()
    #     print "发微博成功~"
    #     time.sleep(5)
    #     self.refresh()
    #
    # #发布微博-好友圈可见-内容：包含链接
    # def test_005_PublishWB(self):
    #     publish = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_compose')
    #     publish.click()
    #
    #     content = config.driver.find_element_by_id("txt-publisher")
    #     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
    #     num = random.randint(1,100)
    #     content.send_keys("http://www.baidu.com" +" " + now + "~")
    #     #设置好友圈可见
    #     # for i in range(1):
    #     #     config.driver.find_element_by_css_selector('a.icon_wbtype.fr').click()
    #     #     time.sleep(1)
    #     #
    #     config.driver.find_element_by_css_selector('a.fr.txt-link').click()
    #     print "发微博成功~"
    #     time.sleep(5)
    #     self.refresh()


    #点赞
    def test_006_ThumbUp(self):
        time.sleep(2)
        box = config.driver.find_elements_by_css_selector('a.box-col.txt-s')
        # print box
        print "type: ", type(box) #list
        print "点赞列表长度: ", len(box)  #30
        tmpList = []
        for i in range(1, len(box) / 3):
            tmpList.append(i * 3 - 1)
        # index = random.choice(tmpList)
        # print index
        print tmpList
        for index in tmpList:
            up = box[index]
            time.sleep(1)
            print index
            up.click()
        # up.click()
        print "点赞成功"
        self.refresh()

    #随机取消点赞
    def test_007_CancelThumbUp(self):

        box = config.driver.find_elements_by_css_selector('a.box-col.txt-s')
        # box = config.driver.find_elements_by_css_selector("i.icon.icon-likedsmall.animated.pulse") # not OK
        print "取消点赞列表长度: ", len(box) #30
        tmpList = []
        for i in range(1, len(box) / 3):
            tmpList.append(i * 3 - 1)
        index = random.choice(tmpList)
        print index
        box[index].click()
        print "取消点赞",(index + 1) / 3, "条微博"
        self.refresh()

    #转发
    def test_008_Forward(self):
        time.sleep(2)
        box = config.driver.find_elements_by_css_selector('a.box-col.txt-s')
        print "box[0] =", box[0]
        print "type: ", type(box) #list
        print "forward len: ",len(box)
        tmpList = []
        for i in range(1, len(box) / 3):
            tmpList.append(i * 3 - 3)
        index = random.choice(tmpList)
        print index
        print "转发第",(index + 3) / 3, "条微博"
        forward = box[index]
        forward.click()
        time.sleep(2)
        #输入转发的内容（可选）
        config.driver.find_element_by_id('txt-publisher').send_keys('test_forward~')
        config.driver.find_element_by_css_selector('a.fr.txt-link').click()
        time.sleep(3)
        print "转发微博成功"
        self.refresh()

    #发布评论
    def test_009_MakeComment(self):
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
       start = time.time()
       print start
       #输入评论
       if config.driver.find_elements_by_css_selector('a.box-col.txt-s'):
           box = config.driver.find_elements_by_css_selector('a.box-col.txt-s')
           print "len:", len(box) #3
           box[1].click()
           print "已有评论的情况~"
           config.driver.find_element_by_id('txt-publisher').send_keys('Thumb Up~')
           end = time.time()
           print end - start
           config.driver.find_element_by_css_selector('a.fr.txt-link').click()
           #返回
           time.sleep(2)
           config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
       else:
           print "还没有评论的情况~"
           config.driver.find_element_by_id('txt-publisher').send_keys('make some comment~')
           end = time.time()
           print end - start
           config.driver.find_element_by_css_selector('a.fr.txt-link').click()
       time.sleep(3)
       print "评论成功"
       self.refresh()


    #收藏
    def test_010_Collect(self):
        box = config.driver.find_elements_by_css_selector('a.operate-box')
        print "len:", len(box) #10
        box[0].click()
        print "PopUp collect window~"
        config.driver.find_element_by_css_selector('a.line-bottom').click()
        print "收藏成功~"

    #搜索全部
    def test_011_Search(self):
        time.sleep(2)
        button = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_search')
        button.click()
        #输入搜索内容
        config.driver.find_element_by_css_selector('input.search.forSearch').send_keys('2013wltest_001')
        #点击搜索
        config.driver.find_element_by_css_selector('span.btn-txt').click()
        print "搜索成功~"
        for i in range(2):
            time.sleep(3)
            config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
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
if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(ProfileModule)#根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    # unittest.TextTestRunner(verbosity=2).run(suite)
    suit = unittest.TestSuite()#定义一个单元测试容器
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ProfileModule))#将测试用例加入到容器中
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    abspath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'html_result'))
    filename = abspath + "/ProfileModule_" + now + ".html" #定义报告存放路径，支持相对路径
    print filename
    fp= file(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='H5主功_首页模块_能测试报告',
        description='Report Descriptions'
    )
    #自动进行测试
    runner.run(suit)


