# -*- coding: utf-8 -*-

import unittest
import urllib
import urllib2

class TestGet(unittest.TestCase):                                #每个功能模块写成一个测试类

    url = 'http://passportapi.15166.com/user/signup'             #所要访问的URL,每个功能模块写一个csv测试表,对应一个url

    def setUp(self):                                             #初始化函数
        pass
    def tearDown(self):                                          #收尾函数
        pass

    def test_wuwei(self):                                        #执行测试功能的函数
        
        info = {'appid': '4e7dHsOyi5QjgpiBiemIreX74f7VgUCg7L', 'username': 'wuweihku', 'password': '123456', 'repassword': '123456'}#所要提交的数据,即csv里的每一行测试用例

        data = urllib.urlencode(info)                            #将信息编码成urllib2能够识别的类型

        req = urllib2.Request(TestGet.url, data)                 #构造请求对象
               
        response = urllib2.urlopen(req)                          #执行post请求

        response_dict = eval(response.read())                    #读取发回的数据,并将字符串转换为字典

        self.assertEqual(response_dict["res"], 10001)            #验证响应码,每个响应码对应csv里的一行测试用例

if __name__ == '__main__':
    unittest.main()
