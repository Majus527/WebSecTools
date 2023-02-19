import time

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from webscan_backend.plugins.check.common import check_ip
from webscan_backend.plugins.common.common import success, error
from webscan_backend.plugins.portscan.portscan import ScanPort


# Create your views here.


@csrf_exempt     # 标识一个视图可以被跨域访问
@login_required
def port_scan(request):
    """
    端口扫描
    """
    ip = request.POST.get('ip')
    # 判断ip是否合法
    if check_ip(ip):
        # 合法
        result = ScanPort(ip).pool()
        # 日志记录
        # MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok!')

    # 不合法
    return error(400, '请填写正确的IP地址', 'error')
