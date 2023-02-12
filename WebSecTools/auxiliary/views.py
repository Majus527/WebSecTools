from django.http import HttpResponse
from django.shortcuts import render
from webscan.models import FingerPrint, FpCategory, Category, Item


# Create your views here.


def welcome(request):
    """欢迎页面"""
    return render(request, 'auxiliary/welcome.html')


def index(request):
    """主页"""
    cms_items = FingerPrint.objects.all()
    categories = FpCategory.objects.all()

    # 取出要添加到导航栏的分类
    category_nav = Category.objects.filter(add_menu=True).order_by('sort')
    # 取出条目
    items = Item.objects.all()

    print(cms_items)

    # 传递给模板的数据
    context = {
        'cms_items': cms_items,
        'categories': categories,
        'category_nav': category_nav,
        'items': items,
    }

    return render(request, "auxiliary/index.html", context)


def navigation(request):
    """安全导航页面"""
    # 取出要添加到导航栏的分类
    category_nav = Category.objects.filter(add_menu=True).order_by('sort')
    # 取出条目
    items = Item.objects.all()
    # 需要传递给模板（templates）的对象
    context = {
        'category_nav': category_nav,
        'items': items,
    }
    return render(request, 'auxiliary/navigation.html', context)


def docs(request):
    """文档页"""
    return render(request, 'auxiliary/docs.html')
