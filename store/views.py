from django.shortcuts import render, HttpResponse
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import Product
from django.shortcuts import *


# 笔记 以隐藏
# Create your views here.
# 创建视图
# def index(request):
#     method = request.method
#     if method == 'GET':
#         content = 'get'
#     elif method == 'POST':
#         content = 'post'
#     print(request.build_absolute_uri())
#     response = HttpResponse(content, )
#
#     return response


# cookie 处理
# def set_cookies(request):
#     content = ' welcome to my first web'
#     key = 'not_robot'
#     code = '123456'  # 验证马可以根据request 进行hash计算
#     # 验证cookies
#     if request.COOKIES.get(key, '') != code:  # 读取cookie 并进行验证
#         # 如果没有cookies 发送 set_cookies + http302 要求重新访问
#         response = HttpResponse()
#         response.set_cookie(key, code)  # 设置cookie
#         response.status_code = 302  # 要求浏览器进行跳转
#         response['Location'] = request.build_absolute_uri()  # 要求重新访问的网址就是本地地址
#     else:
#         response = HttpResponse(content)
#     return response


# user 测试
# def user(request, id, name="index"):
#     content = f'欢迎查看{name}页面当前id是{id}'  # 也可以写成f'欢迎查看{name}页面当前id是%s'%id
#     return HttpResponse(content)


# uplode 上传功能 上传档案范例
# def upload(request, path=""):
#     html = render(request, "upload.html", locals())
#
#     if request.method == "POST":  # 只有在post 模式下才会传输 后端才会解析body
#         file = request.FILES.get("gavin", "")  # 类似字典
#
#         if file:  # 检查文件讯息
#             # 保存到服务器
#             file_path = os.path.join(settings.MEDIA_ROOT, path)
#             file_name = "new_name_" + file.name
#             if not os.path.exists(file_path):  # 判断文件夹是否存在
#                 os.makedirs(file_path)
#             if os.path.exists(file_name):  # 判断文件存在就重新命名
#                 file_name = '_' + file_name
#             # 1.指定保存路径
#
#             # 2. 保存文件到硬碟
#             with open(file_path + file_name, 'wb+') as f:
#                 # f.write(file.read())#不推荐 如果档案过大 会出现记忆体不够的问题
#                 for chunk in file.chunks():  # 大文件处里方式
#                     f.write(chunk)
#             url_path = request.build_absolute_uri()
#             html_suf = " <script>alert(' 上传资料成功 ');</script> <p>文件地址 :  </p> " + url_path + '/' + file_name
#             # <script>alert('  ');</script>  网页弹出提示讯息写法
#             return HttpResponse(html_suf)
#         else:
#
#             back = "<script>alert(' 未输入资料 ');</script>"
#
#             return HttpResponse(back)
#     return html
# 解决csrf 验证问题的方法在 upload.html
# 渲染变量
# def upload(request):
#     template = loader.get_template("upload.html")  # 调用模板引擎
#     context = {"html": "123", "list": [1, 2]}  # 类似print 的功能直接输出
#     html = template.render(context)
#     return HttpResponse(html)

def detail(request):
    """
    商品详情

    """

    id = request.GET.get("id", "")  # 先从request 接收参数
    if not id.isdigit():
        raise Http404()# 首先判断是不是数字不是数字返回404
    obj = get_object_or_404(Product, id=id)  # 然后将参数丢给模型去查询 如果拿到数据渲染模板 如果没有拿到数据返回404

    return render(request, "detail.html", locals())
