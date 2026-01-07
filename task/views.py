from django.shortcuts import render, redirect # 记得导入 redirect
from .models import Task
from .forms import TaskForm # 导入刚才写的表单

def index(request):
    # --- 处理“添加任务”的 Python 逻辑 ---
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() # 这行 Python 代码直接把数据存入数据库！
            return redirect('index') # 添加完后刷新页面
    else:
        form = TaskForm()

    # --- 处理“搜索”和“显示”的逻辑 ---
    all_tasks = Task.objects.all().order_by('deadline') # 按截止日期排序
    
    query = request.GET.get('q')
    if query:
        all_tasks = all_tasks.filter(subject__icontains=query)

    context = {
        'tasks': all_tasks,
        'form': form, # 把表单也发给网页
    }
    return render(request, 'task/index.html', context)