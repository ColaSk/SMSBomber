# -*- encoding: utf-8 -*-
'''
@File    :   browserbase.py
@Time    :   2021/11/25 14:46:25
@Author  :   sk 
@Version :   1.0
@Contact :   kaixuan.sun@boonray.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import time
from selenium import webdriver
from abc import abstractmethod

WEBDRIVER_TYPE_ENUM = {
    "chrome": 1
}

class WebdriverBase(object):

    def __init__(self, type=1):
        self.type = type

class ChromeWebdriver(WebdriverBase):

    def __init__(self, drive_path=None):
        super().__init__(WEBDRIVER_TYPE_ENUM.get('chrome'))
        self.browser = webdriver.Chrome(chrome_options=self._init_option, 
                                        executable_path=drive_path)
    
    @property
    def _init_option(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        return option
    
    @abstractmethod
    def send(self, phone):
        pass

    def __del__(self):
        self.browser.close()


    
class DefaultChromeWebdriver360(ChromeWebdriver):
    """360借贷存在图形验证码, 多次后不可用"""

    def __init__(self, drive_path=None):
        super().__init__(drive_path)
        self.browser.get('https://www.360jie.com.cn/')
    
    def send(self, phone):
        self.browser.find_element_by_name("mobile").send_keys(phone)
        self.browser.find_element_by_id('btnSendCode1').click()
        time.sleep(5)


class DefaultChromeWebdriverPaipaiDai(ChromeWebdriver):

    def __init__(self, drive_path=None):
        super().__init__(drive_path)
        self.enter_register()
    
    def enter_register(self):
        self.browser.get("https://account.ppdai.com/pc/login")
        self.browser.find_element_by_class_name("login_toRegister").click()

    def send(self, phone):
        key = "8263abd"
        self.browser.find_element_by_name("Mobile").send_keys(phone)
        self.browser.find_element_by_name("Password").send_keys(key)
        self.browser.find_element_by_id("getvefydata").click()


class DefaultChromeWebdriverElema(ChromeWebdriver):
    """饿了吗存在滑块验证码, 不可用"""
    def __init__(self, drive_path=None):
        super().__init__(drive_path)
        self.enter_register()
    
    def enter_register(self):
        self.browser.get('https://open.shop.ele.me/openapi/register')
        self.browser.find_element_by_class_name('el-checkbox__inner').click()
        self.browser.find_element_by_xpath("//*[@class='el-button btn-next-step el-button--primary']").click()
    
    def send(self, phone):
        self.browser.find_element_by_class_name('el-input__inner').send_keys(phone)
        self.browser.find_element_by_class_name('btn-verifyCode').click()


class DefaultChromeWebdriverFengHuan(ChromeWebdriver):
    """存在图形验证码, 多次后不可用"""
    def __init__(self, drive_path=None):
        super().__init__(drive_path)
        self.enter_register()
    
    def enter_register(self):
        self.browser.get('https://www.fengwd.com/')
        self.browser.find_element_by_xpath("//*[@class='top-bar-item login-tag']/a").click()
    
    def send(self, phone):
        self.browser.find_element_by_id('mobile_number').send_keys(phone)
        self.browser.find_element_by_xpath("//*[@class='get-sms-captcha blue']").click()


class DefaultChromeWebdriverWozhuliangyuan(ChromeWebdriver):
    """存在时间限制, 60秒后重发"""
    def __init__(self, drive_path=None):
        super().__init__(drive_path)
        self.enter_register()
    
    def enter_register(self):
        self.browser.get('http://m.7799520.com/register.html')
    
    def send(self, phone):
        self.browser.find_element_by_name('mobile').send_keys([phone])
        bu = self.browser.find_elements_by_tag_name('button')
        for i in bu:
            i.click()
            time.sleep(2)
