import json
import os

from django.shortcuts import render
from django.views.decorators import csrf
from django.contrib.auth.decorators import login_required


# 接收POST请求数据
@login_required
def search_post(request):
    import os

    parm = []  # 勾选参数列表
    base_file_path = 'dirscan/dirsearch/reports/target.json'  # json文件地址
    fixes = {}

    # 如果是POST请求，否则直接返回页面
    if request.POST:
        # 获取用户输入的url
        enter_url = ' -u ' + request.POST.get('url') + ' '
        # 获取用户选择的扫描类别
        parm.append(request.POST.get('php'))
        parm.append(request.POST.get('asp'))
        parm.append(request.POST.get('jsp'))
        parm.append(request.POST.get('txt'))
        parm.append(request.POST.get('zip'))
        parm.append(request.POST.get('html'))
        parm.append(request.POST.get('js'))

        p = ''
        for parm in parm:
            if parm is not None:
                parm = parm + ','
                p = parm + p
        options = ' -e ' + p[:-1]  # python dirsearch.py -u xxxx.com -e php,asp...

        # 递归扫描
        recursive = ''
        if request.POST.get('r_check') == "r_yes":
            recursive = '-r' + ' '

        # 前后缀
        # 前缀
        pre_num = 1
        pre = ''
        while request.POST.get('prefixe_' + str(pre_num)) is not None and request.POST.get(
                'prefixe_' + str(pre_num)) != '':
            pre = request.POST.get('prefixe_' + str(pre_num)) + ',' + pre
            pre_num = pre_num + 1
        if pre != '' and pre != ',':
            pre = '--prefixes ' + pre[:-1] + ' '
        else:
            pre = pre[:-1]

        # 后缀
        suf_num = 1
        suf = ''
        while request.POST.get('suffixe_' + str(suf_num)) is not None and request.POST.get(
                'suffixe_' + str(suf_num)) != '':
            suf = request.POST.get('suffixe_' + str(suf_num)) + ',' + suf
            suf_num = suf_num + 1
        if suf != '' and suf != ',':
            suf = '--suffixes ' + suf[:-1] + ' '
        else:
            suf = suf[:-1]

        # 指定子目录扫描
        s_num = 1
        subdir = ''
        while request.POST.get('subdirs_' + str(s_num)) is not None and request.POST.get(
                'subdirs_' + str(s_num)) != '':
            subdir = request.POST.get('subdirs_' + str(s_num)) + '/,' + subdir
            s_num = s_num + 1

        if subdir != '/,' and subdir != '':
            subdir = '--subdirs ' + subdir[:-1] + ' '
        else:
            subdir = subdir[:-2]

        # 清空上次扫描数据
        open(base_file_path, 'w').close()
        # 基础命令拼接
        c = 'python dirscan/dirsearch/dirsearch.py' + \
            options + enter_url + recursive + pre + suf + subdir + \
            '--json-report ' + base_file_path
        print(c)
        os.system(c)
    return render(request, "dirscan/dir-scan.html", fixes)


base_file_path = 'dirscan/dirsearch/reports/target.json'


@login_required
def dirresult(request):
    # 路径是否存在
    if os.access(base_file_path, os.F_OK):
        f = open(base_file_path)
        data = json.load(f)  # json被转换为python字典

        # 获取扫描url的端口等信息，将字典的键转为集合
        k = set(data)
        # 移除集合中的time
        # k.remove('time')
        # 安全移除time
        k.discard('time')
        # 键值集合转为列表
        key_list = list(k)

        # 计数
        n = 0
        for key in data:
            n = n + 1
        # 列表合一
        a = []
        num = 0
        for key in data:
            num = num + 1
            if num < n:
                a = a + data[key]
        print({"a": a, "key_list": key_list})
        return render(request, "dirscan/dir-result.html", {"a": a, "key_list": key_list})
    else:
        error = "暂无结果"
        return render(request, "dirscan/dir-result.html", {"error": error})
