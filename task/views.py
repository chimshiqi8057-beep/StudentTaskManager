from django.shortcuts import render
from .models import Task  # 从 models.py 导入你写的 Task 类

def index(request):
    # 获取数据库里所有的任务
    all_tasks = Task.objects.all()
    # 交给网页模板显示
    return render(request, 'task/index.html', {'tasks': all_tasks})