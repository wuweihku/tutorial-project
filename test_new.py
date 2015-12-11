import unittest
import urllib
import urllib2

class TestGet(unittest.TestCase):

    url = 'http://passportapi.15166.com/user/signup'

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_wuwei(self):
        
        params =urllib.urlencode({'appid': '4e7dHsOyi5QjgpiBiemIreX74f7VgUCg7L', 'username': 'wuweihku', 'password': '123456', 'repassword': '123456'})     
        
        req = urllib2.urlopen(TestGet.url, params)

        content = eval(req.read())

        self.assertEqual(content["res"], 10001)
#######################################################################
    def test_qahechang(self):

        params2 =urllib.urlencode({'appid': '4e7dHsOyi5QjgpiBiemIreX74f7VgUCg7L', 'username': 'qahechang', 'password': '123456', 'repassword': '123456'})
        
        req = urllib2.urlopen(TestGet.url, params2) 

        content2 = eval(req.read())

        self.assertEqual(content2["res"], 10008)

        




if __name__ == '__main__':
    unittest.main()
