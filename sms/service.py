# -*- encoding: utf-8 -*-
'''
@File    :   services.py
@Time    :   2021/11/25 10:30:38
@Author  :   sk 
@Version :   1.0
@Contact :   kaixuan.sun@boonray.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib


class SMSservice(object):

    """一人一服务"""

    def __init__(self, phone, browsers) -> None:
        self.__phone = phone
        self.__browsers = browsers

    def send(self):
        for browser in self.__browsers:
            browser.send(self.__phone)

    def start(self, num=4):
        for i in range(num):
            print(i)
            self.send()
    
    def close(self):
        pass