from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('vulnscan', views.vulnscan, name="vulnscan"),
    path('vuln_scan', views.vuln_scan, name='vuln_scan'),

]

# 动态获取漏洞结果页面
target_ids = views.get_target_id()
vuln_ids = views.get_vuln_id()
for target_id in target_ids:
    urlpatterns.append(url(r'^vuln_result/(?P<target_id>.*)$', views.vuln_result, name='vuln_result/'+target_id))
for vuln_id in vuln_ids:
    urlpatterns.append(url(r'^vuln_detail/(?P<vuln_id>.*)$', views.vuln_detail, name='vuln_detail/' + vuln_id))