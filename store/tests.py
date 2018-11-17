from django.test import *
import unittest


# Create your tests here.
def byte2str(content):
    return str(content, encoding="utf-8")


#@unittest.skip("skip")
class TemplatesTest(TestCase):
    def test_detail(self):
        url = '/temp.html'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # content = byte2str(response.content)
        # self.assertTrue('吊牌价' in content)
        # self.assertTrue('common.css' in content)
