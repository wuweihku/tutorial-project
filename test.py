import unittest
import httplib, urllib 

class TestGet(unittest.TestCase):
    def test_baidu(self):    
        conn = httplib.HTTPConnection("www.baidu.com")
        conn.request("GET", "/index.html") 
        r1 = conn.getresponse() 
        self.assertEqual(r1.status, 200)
        conn.close()
    
    def test_aofei(self):  
        conn = httplib.HTTPConnection("passportapi.15166.com")
        conn.request("GET", "/")
        r2 = conn.getresponse() 
        self.assertEqual(r2.status, 200)
        conn.close()

    def test_register(self):
        params = urllib.urlencode({'appid': 2, 'username': 'wuwei', 'password': '123456', 'repassword': '123456'})     
        conn = httplib.HTTPConnection("passportapi.15166.com")  
        conn.request("POST", "/user/signup", params)
        response = conn.getresponse()  
        self.assertEqual(response.status, 200)
        print response.read()
        conn.close()
if __name__ == '__main__':
    unittest.main()
