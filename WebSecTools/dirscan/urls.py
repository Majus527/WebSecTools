
from django.urls import path
from dirscan import views, target

urlpatterns = [
    path('dir-search/', views.search_post, name="dir-search"),
    path('dir-result/', views.dirresult, name="dir-result"),
    path('get-target/', target.get_target, name="get-target")
]
