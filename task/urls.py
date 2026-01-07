from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 访问首页就运行 index 函数
]