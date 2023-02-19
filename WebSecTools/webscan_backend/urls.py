
from django.urls import path
from webscan_backend import views

urlpatterns = [
    # 端口扫描
    path('port_scan', views.port_scan, name='port_scan'),

]