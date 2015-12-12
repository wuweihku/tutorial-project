# -*- coding: utf-8 -*-
import unittest
import urllib
import urllib2

class TestGet(unittest.TestCase):

    url = 'http://passportapi.15166.com/user/signup'#所要访问的URL

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_wuwei(self):
        
        info = {'appid': '4e7dHsOyi5QjgpiBiemIreX74f7VgUCg7L', 'username': 'wuweihku', 'password': '123456', 'repassword': '123456'}#所要提交的信息

        data = urllib.urlencode(info)#将信息编码成urllib2能过识别的数据

        req = urllib2.Request(TestGet.url, data)#构造请求对象
               
        response = urllib2.urlopen(req)#请求

        the_page = eval(response.read())#读取发回的数据,并将字符串转换为字典

        self.assertEqual(the_page["res"], 10001)#测试断言

if __name__ == '__main__':
    unittest.main()
