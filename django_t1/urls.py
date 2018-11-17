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
# from django.conf.urls import url, include
# from django.contrib import admin
# # from store.views import index
# from store.views import set_cookies, user
#
# urlpatterns = [
#     # url(r'^$',index),#静态路由
#     url(r'^set_cookies$', set_cookies),  # 静态路由
#     url(r'^admin/', admin.site.urls),  # 静态路由
#     # url(r'^store', include('store.urls')),#静态路由
#     # 动态url P 表示捕获到的数字变成遗个叫做id 的参数
#     url(r'blog/(?P<id>[0-9]+)$', user, {"name": "blog_"}),
#     url(r'^user/', include('store.urls'))  # 路由包含使用方法
#
# ]
from django.conf.urls import url, include
from django.views.generic import TemplateView  # TemplateView 内至views

urlpatterns = [
    # 对照下面 如果有人访问这个网址 detail.html 那我们就去渲染detail.html 这个目录
    # 看似相同 不过前面的的是路由讯息（注意要记加^S起始和结束符号)后面的是模板
    url('^addrManage.html$', TemplateView.as_view(template_name="addrManage.html"),),
    url('^detail.html$', TemplateView.as_view(template_name="detail.html"), {"storerecommend": range(5)}),
    url('^index.html$', TemplateView.as_view(template_name="index.html"), ),
    url('^list.html$', TemplateView.as_view(template_name="list.html"),{"productlist":range(12)} ),
    url('^login.html$', TemplateView.as_view(template_name="login.html"), ),
    url('^orderCenter.html$', TemplateView.as_view(template_name="orderCenter.html"), ),
    url('^register.html$', TemplateView.as_view(template_name="register.html"), ),
    url('^shoppingCart.html$', TemplateView.as_view(template_name="shoppingCart.html"), ),
    url('^temp.html$', TemplateView.as_view(template_name="temp.html"), ),
    url(r"^store/", include("store.urls")),
]
