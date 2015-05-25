#coding:utf-8
#把全局变量定义在一个单独的模块中
from appium import webdriver

#define the global variables,other files will use the variable driver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.2LRX22G'
desired_caps['deviceName'] = '小米手机'
#desired_caps['platformVersion'] = '4.2.2'
#desired_caps['deviceName'] = 'Galaxy S4'
desired_caps['browserName'] = 'Chrome'

# Returns abs path relative to this file and not cwd
#desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'apps/com.android.chrome_084652.apk'))
#chrome browser
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

#小米手机自带的浏览器,会自动跳转到使用Chrome浏览器
# desired_caps['appPackage'] =  'com.android.browser'
# desired_caps['appActivity'] = 'com.android.browser.BrowserActivity'

#UC browser  failed: get('url') func not implemented.
# desired_caps['appPackage'] = 'com.UCMobile'
# desired_caps['appActivity'] = 'com.uc.browser.InnerUCMobile'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
# driver.find_element().is_displayed()