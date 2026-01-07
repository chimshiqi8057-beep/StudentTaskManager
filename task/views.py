from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    # --- 逻辑 A: 处理用户点击 "Add Task" 提交的数据 ---
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # 把新任务存入数据库
            return redirect('index')  # 添加完后刷新页面，清空表单
    else:
        form = TaskForm()

    # --- 逻辑 B: 获取数据并排序 (按截止日期升序排列) ---
    all_tasks = Task.objects.all().order_by('deadline')
    
    # --- 逻辑 C: 处理搜索功能 ---
    query = request.GET.get('q') # 获取搜索框输入的内容
    if query:
        # 过滤科目(subject)中包含搜索词的任务
        all_tasks = all_tasks.filter(subject__icontains=query)

    # 把数据发送给 HTML 网页
    context = {
        'tasks': all_tasks,
        'form': form,
    }
    return render(request, 'task/index.html', context)

