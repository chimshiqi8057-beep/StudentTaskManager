from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    # 逻辑 1: 处理添加任务 (POST 请求)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    # 逻辑 2: 获取所有任务并按截止日期(deadline)排序
    tasks = Task.objects.all().order_by('deadline')

    # 逻辑 3: 处理搜索过滤 (根据科目 subject 搜索)
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(subject__icontains=query)

    return render(request, 'task/index.html', {'tasks': tasks, 'form': form})

# 逻辑 4: 处理点击“完成”按钮的函数
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('index')