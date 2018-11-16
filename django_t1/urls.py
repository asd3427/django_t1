"""django_t1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from store.views import index
from store.views import set_cookies, user

urlpatterns = [
    # url(r'^$',index),#静态路由
    url(r'^set_cookies$', set_cookies),  # 静态路由
    url(r'^admin/', admin.site.urls),  # 静态路由
    # url(r'^store', include('store.urls')),#静态路由
    # 动态url P 表示捕获到的数字变成遗个叫做id 的参数
    url(r'blog/(?P<id>[0-9]+)$', user, {"name": "blog_"}),
    url(r'^user/', include('store.urls'))  # 路由包含使用方法

]
