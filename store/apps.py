from django.apps import AppConfig

# 可以有多套配置
class StoreConfig(AppConfig):
    name = 'store'
    verbose_name = "商品数据"
