from django.http import HttpResponse
import json
import re
import socket

from webscan_backend.plugins.check.common import check_url


def success(code=200, data=[], msg='success'):
    """
    返回成功的json数据
    :param code:
    :param data:
    :param msg:
    :return:
    """
    result = {
        'code': code,
        'data': data,
        'msg': msg,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


def error(code=400, data=[], msg='error'):
    """
    返回失败的json数据
    :param code:
    :param data:
    :param msg:
    :return:
    """
    result = {
        'code': code,
        'data': data,
        'msg': msg,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


# 获取用户ip地址
def getuserip(request):
    """
    获取用户IP
    :param request:
    :return:
    """
    try:
        request_ip = request.META['REMOTE_ADDR']
    except KeyError:
        pass
    try:
        # 反向代理后存储的IP
        user_ip = request.META['HTTP_X_FORWARDED_FOR']
    except KeyError:
        # 局域网请求
        user_ip = None
    return user_ip or request_ip


def getdomain(url=''):
    """
    获取域名
    :param url:
    :return:
    """
    url = check_url(url)
    if url:
        domain = url.split('/')[2]  # 获取域名
        print('[LOG GetDomain]: ', domain)
        return domain
    return None
