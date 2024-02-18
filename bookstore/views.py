from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response

from bookstore.models import Book, Tactics, Code
from django.core.paginator import Paginator
from django.forms import model_to_dict


# Create your views here.

def index(request):
    return render(request, 'index.html')


def all_book(request):
    all_books = Book.objects.filter(is_active=True)

    return render(request, 'all_book.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print(e)
        return HttpResponse("The book is not find!")

    if request.method == 'GET':
        return render(request, 'update_book.html', locals())
    elif request.method == 'POST':
        price = request.POST['price']
        market_price = request.POST['market_price']

        book.price = price
        book.market_price = market_price

        book.save()
        return HttpResponseRedirect("/all_book")


def delete_book(request):
    # 通过获取查询字符串 book_id 拿到要删除的book的id
    book_id = request.GET.get("book_id")
    if not book_id:
        return HttpResponse("is not find")
    try:
        obj_book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        return HttpResponse("你要查询的数据错误，代码为： %s" % e)

    obj_book.is_active = False
    obj_book.save()
    return HttpResponseRedirect("/all_book")


def all_code(request):
    all_codes = Code.objects.filter(is_active=True)

    return render(request, "all_code.html", locals())


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    password = request.POST['password']
    username = request.POST['username']
    return HttpResponse("password={},username={}".format(password, username))


def all_tactics(request):
    page_num = request.GET.get('page', 1)
    tactics = Tactics.objects.filter()
    # 初始化Paginator
    paginator = Paginator(tactics, 20)  # tactics是获取的数据，20是指分多少页
    # 初始化具体页码的page对象
    c_page = paginator.page(int(page_num))

    data_list = []
    # 将c_page里面的数据转换成dict格式
    for i in c_page:
        mode_to = model_to_dict(i, exclude='')  # exclude是指去掉哪个字段
        data_list.append(mode_to)

    return render(request, 'all_tactics.html', locals())


from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView


class TacticsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tactics
        fields = "__all__"


class TacticsView(ListCreateAPIView):
    queryset = Tactics.objects.all()
    serializer_class = TacticsSerializers


class TacticsDetailView(RetrieveAPIView):
    queryset = Tactics.objects.all()
    serializer_class = TacticsSerializers
