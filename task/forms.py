from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # 在网页上显示的字段
        fields = ['title', 'subject', 'deadline', 'priority']
        # 优化日期选择器，让它显示日历控件
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }