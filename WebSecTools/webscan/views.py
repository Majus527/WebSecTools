from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from webscan.models import PortList, FingerPrint, FpCategory


# Create your views here.


@login_required
def portscan(request):
    """端口扫描"""
    portlists = PortList.objects.all()  # 常用端口列表
    context = {'portlists': portlists}
    return render(request, 'scan/scan_portscan.html', context)


@login_required
def fingerprint(request):
    """指纹识别"""
    cms_items = FingerPrint.objects.all()
    categories = FpCategory.objects.all()
    context = {
        'cms_items': cms_items,
        'categories': categories,

    }
    return render(request, 'scan/scan_fingerprint.html', context)


@login_required
def subdomain(request):
    """子域名扫描"""
    return render(request, 'scan/scan_subdomain.html')


@login_required
def webside(request):
    """旁站扫描"""
    return render(request, 'scan/scan_webside.html')


@login_required
def infoleak(request):
    """信息泄露"""
    return render(request, 'scan/scan_infoleak.html')
