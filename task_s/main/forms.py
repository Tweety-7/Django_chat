from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "sponsor", "recipient"]
        wigets = {
            "title": TextInput(attrs={'plaseholder': 'Введите название'}),
            "task": Textarea(attrs={'placeholder': 'Введите сообщение'}),
            "sponsor": TextInput(attrs={'placeholder': 'от кого сообщение'}),
            "recipient": TextInput(attrs={'placeholder': 'кому сообщение'})
        }
# Class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
    # class Meta:
    #     fields = ('username', 'email', 'password1', 'password2', )
