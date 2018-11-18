from django.conf.urls import url
from .views import detail

urlpatterns = [
    # url(r'^upload$', upload),
    # url(r'upload_pic$', upload, {"path": "pic"}),
    # url(r'upload_html$', upload, {"path": "html"}),
    # url(r'upload_js$', upload, {"path": "js"}),
    # url(r'^(?P<id>[0-9]+)$', user, {"name": "_chen"}),
    # url(r'^login$', user, {"name": "_chen", "id": ""}),  # 这三个url 前缀是一样的
    # url(r'^reg$', user, {"name": "_chen", "id": ""}),  # 这三个url 前缀是一样的
    # url(r'^logout$', user, {"name": "_chen", "id": ""}),  # 这三个url 前缀是一样的
    url(r'detail.html', detail)
]
