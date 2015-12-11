import unittest
import urllib
import urllib2

class TestGet(unittest.TestCase):
    def test_register(self):
        
        params =urllib.urlencode({'appid': '4e7dHsOyi5QjgpiBiemIreX74f7VgUCg7L', 'username': 'wuweihku', 'password': '123456', 'repassword': '123456'})     
        
        url = 'http://passportapi.15166.com/user/signup'

        req = urllib2.urlopen(url, params)

        content = eval(req.read())

        self.assertEqual(content["res"], 10008)
#######################################################################
        params2 =urllib.urlencode({'appid': '4e7dHsOyi5QjgpiBiemIreX74f7VgUCg7L', 'username': 'qahechang', 'password': '123456', 'repassword': '123456'})
        
        req = urllib2.urlopen(url, params2) 

        content2 = eval(req.read())

        self.assertEqual(content2["res"], 10008)

        




if __name__ == '__main__':
    unittest.main()
