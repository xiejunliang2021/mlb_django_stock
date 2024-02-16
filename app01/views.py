# from django.shortcuts import render,HttpResponse
# # import oracledb
# import conn
#
#
#
# # Create your views here.
#
# conn_ = conn.Conn()
#
#
# def index(request):
#     return HttpResponse("welcome to my stockquant!")
#
#
# def user_list(request):
#     # 去app目录下的templates寻找，那么首先要在app的目录下创建templates文件夹
#     # 优先在根目录下寻找，然后在其他的app中寻找，如果找不到最后在去外部的templates中寻找
#     return render(request,"user_list.html")
#
# def page_name(request,name):
#     return HttpResponse("this is page {} !".format(name))
#
# def page_clm(requres,m,clm,n):
#     if clm not in ["add", "min", "mul"]:
#         return HttpResponse("sorry! It's wrong! You must be [sum,min,mul]")
#     elif clm == "add":
#         result = m + n
#     elif clm == "min":
#         result = m - n
#     elif clm == "mul":
#         result = m * n
#     else:
#         result = 0
#     return HttpResponse("您输入的结果为 {} !".format(result))
#
#
# def test_clm(request):
#     if request.method == 'GET':
#         return render(request,"mycal.html")
#     # 处理计算
#     result = 0
#     x = float(request.POST['x'])
#     y = float(request.POST['y'])
#     op = request.POST['op']
#     if op == "add":
#         result = x + y
#     elif op == "sub":
#         result = x - y
#     elif op == "mul":
#         result = x * y
#     else:
#         if y == 0:
#             return render(request,"error.html")
#         else:
#             result = x / y
#
#     return render(request,"mycal.html",locals()) # locals函数是将局部变量封装乘字典进行传递
#
# def transfer_arg(request):
#     dic = {}
#     dic['name'] = "xiejunliang"
#     dic["age"] = 35
#     dic['lis_friends'] = ["Lily", "Hanmeimei", "Lucy", "Jim"]
#     dic['lis_stock'] = get_code_tactics
#     return render(request,"传参数.html", dic)
#
#
# def get_code_tactics():
#     con = conn_.conn_jap()
#     cur = con.cursor()
#     sql = "select * from new_tactics where trade_date between to_date('20230502','yyyy-mm-dd') and to_date('20230602','yyyy-mm-dd') "
#     res = cur.execute(sql).fetchall()
#     # print(res)
#     cur.close()
#     con.close()
#
#     return res
#
#
#
#
