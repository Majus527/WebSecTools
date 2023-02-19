# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from django.contrib.auth.decorators import login_required


# 接收POST请求数据
@login_required
def search_post(request):
    return render(request, "dirscan/dir-scan.html")


