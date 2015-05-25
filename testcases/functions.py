#coding:utf-8

import time
import config

def login():
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


if __name__ == "__main__":
    login()

