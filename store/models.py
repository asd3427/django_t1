from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Brand(models.Model):
    title = models.CharField("品牌名称", max_length=200)

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField("分类名称", max_length=200)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Product(models.Model):  # 继承于django模型
    GENDER_CHOICES = (
        (1, "男士"),
        (2, "女士"),
        (3, "情侣"),
    )
    TYPE_CHOICES = (
        (1, "上装"),
        (2, "下装"),
        (3, "鞋履"),
        (4, "配饰"),
    )

    title = models.CharField("商品名称", max_length=200, help_text="输入商品名称")  # 字符型态
    # 分类 一对多 每个分类有多个商品 一对多时 第一个参数要写我们自己写的类（Category）
    #  on_delete是django 2.0 才开始要写的关联方法 意思就是如果有关连的时候就不予许删除
    # 先设定為空 null=True
    category = models.ForeignKey(Category, verbose_name="所属分类", on_delete=models.PROTECT, null=True)
    """
    DecimalField 小数记量高精度用于计算金额 decimal_places=2 小数点后的位数
    max_digits=8 总的长度
    validators=[MinValueValidator(0) 验证器 验证最小数值為0
    """
    brand = models.ForeignKey(Brand, verbose_name="所属品牌", on_delete=models.PROTECT, null=True)

    price = models.DecimalField("吊牌价", default=0, decimal_places=2, max_digits=8,
                                validators=[MinValueValidator(0), ])

    sales_price = models.DecimalField("销售价", default=0, decimal_places=2, max_digits=8,
                                      validators=[MinValueValidator(0), ], help_text="输入价格不可小于0")

    sales_count = models.IntegerField("销量", default=0, validators=[MinValueValidator(0), ])

    num = models.IntegerField("库存", default=0, validators=[MinValueValidator(0), ])

    discount = models.IntegerField("折扣比例", default=100, validators=[MinValueValidator(1), MaxValueValidator(100)],
                                   help_text="填写1～100,100表示原价")

    # size = models.ForeignKey(Size, on_delete=models.PROTECT, verbose_name="尺码")
    # 资料库内存的是整数
    gender = models.IntegerField("性别", default=1, choices=GENDER_CHOICES, db_index=True)

    type = models.IntegerField("类型", default=1, choices=TYPE_CHOICES, db_index=True)

    content = RichTextUploadingField("商品详情", null=True, blank=True)  # 附文本可存较大的文字量

    def get_discount_display(self):
        return self.discount / 10

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ProductPic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="商品", related_name="pic")
    title = models.CharField("商品标题", max_length=200)
    is_main = models.BooleanField("主图", default=False)
    order = models.IntegerField("序号", default=0, help_text="数字越小,位址越前")
    img = models.ImageField("图片地址", )

    class Meta:
        verbose_name = "商品图片列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title + f'(商品ID = {self.product_id})'
