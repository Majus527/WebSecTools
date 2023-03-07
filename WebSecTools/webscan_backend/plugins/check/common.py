import re

# 禁止扫描的IP
FORBIDDEN_IP_RULE = '(^0\.0\.0\.0$)' \
                    '|(120.55.58.175)' \
                    '|(^10\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])$)' \
                    '|(^127\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])$)' \
                    '|(^172\.(1[6789]|2[0-9]|3[01])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])$)' \
                    '|(^192\.168\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])$)'

# 禁止扫描的域名
FORBIDDEN_DOMAIN = '(127.0.*.*)' \
                   '|(^192\.168\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])$)' \
                   '|(local)|(gov.cn)'


def check_ip(ipaddr=''):
    """
    校验IP合法性
    :param ipaddr:
    :return: True|False
    """
    ipaddr = (str(ipaddr)).strip()  # strip移除字符串头尾指定的字符（默认为空格或换行符）
    # IP地址的长度范围(6, 16)
    if (6 < len(ipaddr)) and (len(ipaddr) < 16):
        # 判断是否在禁止IP列表中
        if re.search(FORBIDDEN_IP_RULE, ipaddr):
            return True
        # ip地址都是（1~255）.（0~255）.（0~255）.（0~255）的格式
        rule = r'^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$'
        compile_ip = re.compile(rule)
        if compile_ip.match(ipaddr):
            return True
    return False


def check_url(url=''):
    """
    校验URL合法性
    :param url:
    :return: 合法的URL | False
    """
    url = (str(url)).strip().replace('"', '').replace("'", '').replace('<', '').replace('>', '').replace(';', '')\
        .replace('\\', '/')
    if (10 < len(url)) and (len(url) < 40):
        # 链接长度(10, 40)，否则认为不合法 http://a.cn
        if re.search(FORBIDDEN_DOMAIN, url):
            # 判断是否在禁止域名/IP
            return True
        if url.startswith('http://') or url.startswith('https://'):
            # URL是否以http://或https://开头
            url_params = url.split('/')
            domain = url_params[2]
            if domain.find('.') >= 0:
                # URL中的域名是否至少含有一个‘.’，返回全小写URL
                return url.lower()
    return False
