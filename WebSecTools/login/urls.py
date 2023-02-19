
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),         # 注册模块
    path('login/', views.login, name="login"),                  # 登录模块
    path('password-reset/', include('password_reset.urls'), name='password_reset'),     # 重置密码
    path('login_out/', views.login_out, name="login_out"),      # 注销账号

]
