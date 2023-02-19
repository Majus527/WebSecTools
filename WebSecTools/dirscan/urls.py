
from django.urls import path
from dirscan import views, do_search

urlpatterns = [
    path('dir-search/', do_search.search_post, name="dir-search"),
]
