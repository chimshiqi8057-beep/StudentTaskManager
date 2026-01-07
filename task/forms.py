from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # 告诉 Python 我们要在网页上显示的字段
        fields = ['title', 'subject', 'deadline', 'priority']
        # 让日期选择器看起来更像样
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }