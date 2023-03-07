import json
import re
import time

from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from WebSecTools.settings import API_KEY, API_URL
from vulnscan.API.Scan import Scan
from vulnscan.API.Target import Target
from vulnscan.API.Vuln import Vuln
from vulnscan.models import Middleware_vuln
from webscan_backend.plugins.common.common import success, error


# Create your views here.


@login_required
def vulnscan(request):
    s = Scan(API_URL, API_KEY)
    data = s.get_all()
    count = 0
    s_list = []
    Middleware_datas = Middleware_vuln.objects.all()[::-1]
    for Middleware in Middleware_datas:
        # print(Middleware.url, Middleware.CVE_id, Middleware.result, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(Middleware.time))))
        result = 1 if Middleware.result == "True" else 0
        Middleware_data = {
            'id': count + 1,
            'status': Middleware.status,
            'target_id': None,
            'target': Middleware.url,
            'scan_type': Middleware.CVE_id,
            'vuln': {'high': result, 'medium': 0, 'low': 0, 'info': 0},
            'plan': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(Middleware.time)))
        }
        s_list.append(Middleware_data)
        count += 1
    for msg in data:
        table_data = {
            'id': count + 1,
            'status': msg['current_session']['status'],
            'target_id': msg['target_id'],
            'target': msg['target']['address'],
            'scan_type': msg["profile_name"],
            'vuln': msg['current_session']['severity_counts'],
            'plan': re.sub(r'T|\..*$', " ", msg['current_session']['start_date'])
        }
        s_list.append(table_data)
        count += 1
    data = s_list
    return render(request, "vulnscan/vulnscan.html", {"data": data})


@csrf_exempt
def vuln_scan(request):
    url = request.POST.get('ip')
    scan_type = request.POST.get('scan_type')
    t = Target(API_URL, API_KEY)
    target_id = t.add(url)
    if target_id is not None:
        s = Scan(API_URL, API_KEY)
        status_code = s.add(target_id, scan_type)
        if status_code == 200:
            return success()
    return error()


@login_required
def vuln_result(request, target_id):
    d = Vuln(API_URL, API_KEY)
    data = []
    vuln_details = json.loads(d.search(None,None, "open", target_id=str(target_id)))

    id = 1
    for target in vuln_details['vulnerabilities']:
        item={
            'id': id,
            'severity': target['severity'],
            'target': target['affects_url'],
            'vuln_id':target['vuln_id'],
            'vuln_name': target['vt_name'],
            'time': re.sub(r'T|\..*$', " ", target['last_seen'])
        }
        id += 1
        data.append(item)
    return render(request,'vulnscan/vuln-reslut.html',{'data': data})


def get_target_id():
    s = Scan(API_URL, API_KEY)
    data = s.get_all()
    target_list = []
    for target in data:
        target_list.append(target['target_id'])
    return target_list


def get_vuln_id():
    d = Vuln(API_URL,API_KEY)
    data = d.get_all("open")
    vuln_list = []
    try:
        for vuln in data['vulnerabilities']:
           vuln_list.append(vuln['vuln_id'])
    except:
        pass
    return vuln_list


@login_required
def vuln_detail(request,vuln_id):
    d = Vuln(API_URL,API_KEY)
    data = d.get(vuln_id)
    print(data)
    parameter_list = BeautifulSoup(data['details'], features="html.parser").findAll('span')
    request_list = BeautifulSoup(data['details'], features="html.parser").findAll('li')
    data_dict = {
        'affects_url': data['affects_url'],
        'last_seen': re.sub(r'T|\..*$', " ", data['last_seen']),
        'vt_name': data['vt_name'],
        'details': data['details'].replace("  ",'').replace('</p>',''),
        'request': data['request'],
        'recommendation': data['recommendation'].replace('<br/>','\n')
    }
    try:
        data_dict['parameter_name'] = parameter_list[0].contents[0]
        data_dict['parameter_data'] = parameter_list[1].contents[0]
    except:
        pass
    num = 1
    try:
        Str = ''
        for i in range(len(request_list)):
            Str += str(request_list[i].contents[0])+str(request_list[i].contents[1]).replace('<strong>', '').replace('</strong>', '')+'\n'
            num += 1
    except:
        pass
    data_dict['Tests_performed'] = Str
    data_dict['num'] = num
    data_dict['details'] = data_dict['details'].replace('class="bb-dark"','style="color: #ff0000"')
    return render(request, "vulnscan/vuln-detail.html", {'data': data_dict})