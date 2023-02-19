
from django.urls import path
from django.views.generic import TemplateView


from webscan import views


urlpatterns = [
    # 端口扫描
    path('portscan', views.portscan, name='portscan'),
    # 指纹识别
    path('fingerprint', views.fingerprint, name='fingerprint'),
    # 子域名探测
    path('subdomain', views.subdomain, name='subdomain'),
    # 旁站扫描
    path('webside', views.webside, name='webside'),
    # 信息泄露
    path('infoleak', views.infoleak, name='infoleak'),
]