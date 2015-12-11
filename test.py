import unittest
import urllib 
import http.client

class TestGet(unittest.TestCase):
    def test_register(self):
        params = urllib.parse.urlencode({'appid': '4e7dHsOyi5QjgpiBiemIreX74f7VgUCg7L', 'username': 'wuwei', 'password': '123456', 'repassword': '123456'})     
        print(params)
        conn = http.client.HTTPConnection("passportapi.15166.com")  
        conn.request("POST", "/user/signup", params)
        response = conn.getresponse()  
        self.assertEqual(response.status, 200)
        data = eval(response.read())
        print(data)
        self.assertEqual(data["res"], 10002)
        conn.close()
if __name__ == '__main__':
    unittest.main()
