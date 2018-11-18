from django.test import *
import unittest
from store.models import Product
import random


#
# Create your tests here.
def byte2str(content):
    return str(content, encoding="utf-8")


class StoreViewsTest(TestCase):
    """
    1.在资料库裡保存数据 Model
    2.访问/store/detail.html?id={id}网址可以访问到讯息
    3.根据不同id页面上显示的讯息不一样 分别和数据库的数据一致
    """

    def setUp(self):
        # 创建数据，准备测试环境
        self.mock_data = []

        for i in range(3):
            self.mock_data.append(Product.objects.create(title=f"新的标题{i} {random.randint(1,10)}"))
        pass

    def tearDown(self):
        # 删除测试数据
        Product.objects.all().delete()
        print("清理数据完成")

    def test_detail(self):
        """测试商品页渲染页面"""
        for obj in self.mock_data:  # 查找数据库中的模型
            url = f"/store/detail.html?id={obj.id}"
            response = self.client.get(url) # 访问本项目url
            self.assertEqual(response.status_code, 200, "详情页访问失败")

            content = byte2str(response.content)
            self.assertTrue("吊牌价" in content, "吊牌价渲染出错")  # 判断模板有没有选错
            self.assertTrue(obj.title in content, "商品名称出错")
            self.assertTrue("detail.css" in content, "商品样式表未加载")  # 判断样式文件是否正确


@unittest.skip("该功能已废弃，跳过测试")
def test_index(self):
    url = "/"
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

    content = byte2str(response.content)
    self.assertTrue("商城首页" in content)
    self.assertTrue("index.css" in content)
