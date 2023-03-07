
from django.urls import path
from webscan_backend import views

urlpatterns = [
    # 端口扫描
    path('port_scan', views.port_scan, name='port_scan'),
    # 指纹识别
    path('webweight', views.webweight, name='webweight'),
    path('iswaf', views.is_waf, name='iswaf'),
    path('whatcms', views.what_cms, name='whatcms'),
    path('baseinfo', views.baseinfo, name='baseinfo'),
    path('isexistcdn', views.isexistcdn, name='cdncheck'),
    # 子域名探测
    path('_subdomain', views._subdomain, name='_subdomain'),
    # 旁站扫描
    path('web_side', views.getwebsideinfo, name='web_side'),
    path('web_side', views.getwebsideinfo, name='web_side'),
    path('iplocating', views.iplocating, name='iplocating'),
    # 信息泄露
    path('info_leak', views.info_leak, name='info_leak'),
]