# -*- coding: utf-8 -*-
import unittest                                                 
import urllib.parse                                                                  #这里urllib.parse要导入到子模块,否则会报错
import urllib.request                                                                #这里urllib.request要导入到子模块,否则会报错
import csv


class test_register(unittest.TestCase):                                              #每个功能模块写成一个测试类
    url = 'http://passportapi.15166.com/user/signup'                                 #所要访问的URL,每个功能模块写一个csv测试表,对应一个url
    def test_register_cases(self):                                                   #执行测试功能的函数
        info = {'appid': row['appid'], 'username': row['username'], 'password': row['password'], 'repassword': row['repassword']}#所要提交的数据,即csv里的每一行测试用例
        data = urllib.parse.urlencode(info).encode(encoding='UTF8')                 #将信息编码成urllib能够识别的类型,注意的是python2.7用的ASCII编码,python3.X要UTF8转码
        req = urllib.request.Request(test_register.url, data)                       #构造请求对象         
        response = urllib.request.urlopen(req)                                      #执行post请求
        response_dict = eval(response.read())                                       #读取发回的数据,并将字符串转换为字典
        self.assertEqual(response_dict["res"], eval(row['res']))                    #验证响应码,每个响应码对应csv里的一行测试用例


if __name__ == '__main__':
    suite = unittest.TestSuite()                                                    #用来装用例的suite    
    with open('register_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        caseNum=0                                                                   #记录当前是第几个测试用例
        for row in reader:
            print(row['res'])
            suite.addTest(test_register('test_register_cases'))                                          #每次循环,读取一行字典数据,并作为用例加入suite.其中test_register是测试类的类名           
            unittest.TextTestRunner(verbosity=2) 
unittest.TextTestRunner(verbosity=2).run(suite) 
#unittest.main()






