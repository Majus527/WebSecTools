from django.urls import path

from auxiliary import views

urlpatterns = [
    path('', views.welcome, name='welcome'),    # 欢迎页
    path('index', views.index, name="index"),   # 首页
    path('navigation', views.navigation, name='navigation'),  # 导航页面
    path('docs', views.docs, name='docs'),  # 文档页
    path('about', views.about, name='about'),   # 关于页

]
