from .models import Tasks
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
    
class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['task']
        
        widgets = {
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите задачу'
            })
        }