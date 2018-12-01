from django.contrib import admin
from .models import Product, Category, ProductPic,Brand

# Register your models here.
"""
register(self,         model_or_iterable,         admin_class=None, **options)
          我们定义的模型  可迭代 可多个模型使用一各类    可以指定具体怎展示
"""

admin.site.register(Category)
admin.site.register(ProductPic)
admin.site.register(Brand)

class ProductPicInline(admin.StackedInline):
    model = ProductPic # 那个模型内取数据
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "gender", "type", "brand", "sales_price", "sales_count", "num",
                    "__str__", "get_gender_display", "new_title")  # 显示
    list_filter = ("category", "gender", "type", "brand",)  # 过滤
    search_fields = ("title",)  # 搜索什么
    exclude = ("created",)  # 省略那个字段
    inlines = [ProductPicInline, ]  # 内部关联

    def new_title(self, obj):
        return f"xxx_{obj.title}_ooo"

    new_title.short_description = "新标题"


admin.site.register(Product, admin_class=ProductAdmin)
