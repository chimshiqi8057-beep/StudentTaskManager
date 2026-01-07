from django.urls import path
from . import views

urlpatterns = [
    # 首页路径
    path('', views.index, name='index'),
    # 点击完成按钮触发的路径，<int:task_id> 用来识别是哪一个任务
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]