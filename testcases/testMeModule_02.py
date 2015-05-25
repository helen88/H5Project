#coding:utf-8
"""
This Module is :
- Me Module
-entrance: under "Me" Tab
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


class MeModule(unittest.TestCase):
    "Class to run tests against the chrome browser"
    def setUp(self):
        "Setup for the test"
        pass

    def tearDown(self):
        "Tear down the test"
        # self.config.driver.quit()#执行完后退出应用
        # try:
        #     box = config.driver.find_elements_by_css_selector('a.item.box-col')
        #     self.assertEqual(len(box),4, "返回到主页-我")
        # except:
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

    #我-收藏-取消收藏
    def test_002_CancelCollect(self):
        time.sleep(3)
        box = config.driver.find_elements_by_css_selector('a.item.box-col')
        print len(box)#4
        #点击 我
        box[3].click()
        print "点击 我"
        lists = config.driver.find_elements_by_css_selector('span.mct-a ')
        print len(lists)#7
        lists[4].click()
        print "点击 我的收藏"
        time.sleep(2)
        # collect_list = config.driver.find_elements_by_css_selector('a.operate-box')
        collect_list = config.driver.find_elements_by_css_selector('i.icon-font.icon-font-arrow-down.txt-s')
        if len(collect_list) == 0:
            print "当前没有收藏的微博~"
            #返回
            # time.sleep(3)
            config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
            print "返回到 我"
        else:
            print "当前有收藏微博数目:",len(collect_list) #10
            index = random.choice(range(len(collect_list)))
            print "取消收藏第" + str(index+1) + "条微博"
            collect_list[index].click()
            print "PopUp cancel collect window~"
            config.driver.find_element_by_css_selector('a.line-bottom').click()
            print "取消收藏成功~"
            #返回
            time.sleep(3)
            config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
            print "返回到 我"

    #我-微博-删除自己的微博
    def test_003_DeleteWB(self):
        box = config.driver.find_elements_by_css_selector('a.box-col.line-separate')
        print len(box) #3
        #点击 微博
        box[0].click()
        collect_list = config.driver.find_elements_by_css_selector('i.icon-font.icon-font-arrow-down.txt-s')
        print len(collect_list) #10
        index = random.choice(range(len(collect_list)))
        # print "删除第" + str(index+1) + "条微博"
        collect_list[index].click()
        print "PopUp cancel window~"
        time.sleep(2)
        config.driver.find_element_by_xpath('/html/body/div[2]/div/section/a[2]').click()
        print "删除第" + str(index+1) + "条微博"
        time.sleep(3)
        alert = config.driver.switch_to.alert
        assert '确定要删除这条微博？' in alert.text
        alert.accept()
        config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
        print "返回到 我"

    #加关注(添加或者取消关注:取一个用户来进行这样的一对操作)
    #顶部搜索框-用户-输入用户昵称
    def test_004_Follow(self):
        search = config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_search')
        search.click()
        time.sleep(1)
        box = config.driver.find_elements_by_css_selector('a.item.box-col')
        print len(box)#3
        box[1].click()
        input = config.driver.find_element_by_css_selector('input.search.forSearch')
        input.send_keys("2013wltest_007")
        #点击搜索
        config.driver.find_element_by_css_selector('span.btn-txt').click()
        time.sleep(2)
        #点击加关注
        config.driver.find_element_by_css_selector('i.icon-font.icon-font-follow').click()
        print "关注成功"


    #取消关注
    #接上一case-进入个人主页-已关注-取消关注
    def test_005_CancelFollow(self):
        #点击进入个人主页
        config.driver.find_element_by_css_selector('div.item-main.txt-m.mct-a.txt-cut').click()
        print "进入个人主页~"
        #点击 相互关注或者已关注
        buttons = config.driver.find_elements_by_css_selector('button.btn.btn-normal')
        buttons[1].click()
        time.sleep(1)
        config.driver.find_element_by_xpath('//*[@id="J-action"]/p/a[1]').click()
        time.sleep(1)
        config.driver.find_element_by_id('J-alertPop-confirm').click()
        print "取消关注 成功"
        for i in range(3):
            time.sleep(2)
            config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
        print "返回到 我"


    #设置
    #1、我 - 进入设置-->个人资料、隐私设置页
    #2、任意修改选项，点击【保存】
    #结果：保存成功
    def test_006_Setting(self):
        config.driver.find_element_by_css_selector('a.fr.iconf.iconf_navbar_setting').click()
        print "点击设置按钮"
        lists = config.driver.find_elements_by_css_selector('span.mct-a')
        print len(lists)#9
        lists[0].click()
        print "点击个人资料"
        config.driver.find_element_by_css_selector('select#sex.L-list-select').click()
        print "点击 性别下拉菜单"
        options = config.driver.find_elements_by_tag_name('option')
        # print len(options)#255
        index = random.choice(range(2))
        options[index].click()
        if index == 1:
           print "选择 女"
        else:
           print "选择 男"
        config.driver.find_element_by_css_selector('p#J_summary.J_label').click()
        time.sleep(2)
        #简介
        content = config.driver.find_element_by_name('description')
        content.clear()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") #timestamp
        content.send_keys(u'大白的快乐生活' + now)
        config.driver.find_element_by_id('finish').click()
        #点击保存按钮
        time.sleep(2)
        config.driver.find_element_by_css_selector('a#save.btn-info-page.BtnGreenLev1').click()
        print "保存成功"
        #保存成功的验证:弹窗的处理,内容判断-保存成功
        alert = config.driver.switch_to.alert
        print alert
        time.sleep(3)
        #modal dialog
        assert '保存成功' in alert.text
        alert.accept()#相当于点弹窗里的确定按钮

        config.driver.find_element_by_id('gohome').click()
        config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
        print "返回到 我"

    #发现
    def test_007_Discover(self):
        box = config.driver.find_elements_by_css_selector('a.item.box-col')
        print len(box)#4
        #点击 发现
        box[2].click()
        print "点击 发现"
        box2 = config.driver.find_elements_by_css_selector('a.item-box.line-separate')
        print len(box2)#4
        box2[3].click()
        print "点击 热门话题"
        time.sleep(2)
        config.driver.find_element_by_css_selector('a.fl.iconf.iconf_navbar_back').click()
        print "返回到 发现"


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
    # suite = unittest.TestLoader().loadTestsFromTestCase(MeModule)#根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    # unittest.TextTestRunner(verbosity=2).run(suite)
    suit = unittest.TestSuite()#定义一个单元测试容器
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(MeModule))#将测试用例加入到容器中
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    abspath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'html_result'))
    filename = abspath + "/MeModule_" + now + ".html" #定义报告存放路径，支持相对路径
    print filename
    fp= file(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='H5主功能_我模块_测试报告',
        description='Report Descriptions'
    )
    #自动进行测试
    runner.run(suit)


