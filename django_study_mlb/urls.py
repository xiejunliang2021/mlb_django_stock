"""
URL configuration for django_study_mlb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import bookstore.views
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # index/ 是导航参数   views.index 后面的index是views中的index函数，必须要在views中创建index函数
    # path('index/', views.index),
    # path('user/list/',views.user_list),
    # path('page/<int:name>',views.page_name),
    # path('page/<int:m>/<str:clm>/<int:n>',views.page_clm),
    # path('mycal', views.test_clm),
    # path('transfer_arg', views.transfer_arg),
    path('', bookstore.views.index),
    path('all_book', bookstore.views.all_book),
    path('update_book/<int:book_id>', bookstore.views.update_book),
    path('delete_book', bookstore.views.delete_book),
    path("all_code", bookstore.views.all_code),
    path('login', bookstore.views.login),
    path('tactics', bookstore.views.all_tactics),
    # path('test_page', bookstore.views.test_page),
    # path('test_tac', bookstore.views.test_tactics)
    path("api/stocks/", bookstore.views.TacticsView.as_view()),
    re_path("api/stock/(?P<pk>\d+)", bookstore.views.TacticsDetailView.as_view())
]
