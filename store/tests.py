from django.test import *
import unittest
from store.models import Product,Category
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
        new_cate = Category.objects.create(title="新的分类")
        self.mock_data = []

        for i in range(3):
            self.mock_data.append(Product.objects.create(title=f"新的标题{i} {random.randint(1,10)}",category=new_cate))
        pass

    def tearDown(self):
        # 删除测试数据
        Product.objects.all().delete()
        print("清理数据完成")

    def test_detail(self):
        """测试商品页渲染页面"""

        for id in ('0', 'xx', '9999'):
            if id.isdigit():
                self.assertEqual(0, Product.objects.filter(id=id).count())  # 为了严谨，测试前验证id确实不存在
            url = f"/store/detail.html?id={id}"
            response = self.client.get(url)
            self.assertTrue(404, response.status_code)  # 输入错误的id，响应404

        for obj in self.mock_data:  # 遍历数据库中数据

            url = f"/store/detail.html?id={obj.id}"
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, "详情页访问失败")  # 输入错正确的id，响应404
            self.assertTemplateUsed(response, "detail.html")  # 使用django TESECASE 的断言

            content = byte2str(response.content)

            self.assertTrue("detail.css" in content, "商品样式表未加载")

            # 验证html元素渲染的数据正确

            self.assertTrue(f"""<h4 class="product-name">{obj.title}</h4>""" in content)
            self.assertContains(response, f"""<ol class="breadcrumb">
     	<li>
     		<a href="#">首页</a>
     	</li>
     	<li>
     		<a href="#">{ obj.get_gender_display()}</a>
     	</li>
     	<li>
     		<a href="#">{ obj.get_type_display() }</a>
     	</li>
     	<li class="active">{ obj.category.title}</li>
     </ol>""", status_code=200, html=True)  # 性别、类型、分类 测试失败的话记得改模板

            #self.assertTrue(f"""吊牌价：<span class="old-price">{obj.pric}</span>""" in content)
            #self.assertTrue(f"""促销价：<span class="new-price">{ obj.sales_pric }</span>""" in content)
            self.assertTrue(f"""<span class="discount">{ obj.discount/10}折</span>""" in content)  # 折扣在数据库中存储整数，这里需要换算
            self.assertTrue(f"""<div class="container product-all-msg">{ obj.content }</div>""" in content)  # 详情


@unittest.skip("该功能已废弃，跳过测试")
def test_index(self):
    url = "/"
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

    content = byte2str(response.content)
    self.assertTrue("商城首页" in content)
    self.assertTrue("index.css" in content)
