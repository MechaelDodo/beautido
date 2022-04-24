from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddGirlForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Girl
        fields = ['title', 'slug', 'content', 'photo', 'category']   #'__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', }),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title
    #title = forms.CharField(max_length=255, label='Имя и фамилия',
    #                        widget=forms.TextInput(attrs={'class': 'form-input', }))
    #slug = forms.SlugField(max_length=255, label='Url')
    #content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание')
    #is_published = forms.BooleanField(required=False, initial=True)
    #category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
    #                                  empty_label='Категория не выбрана')


# class AddScore(forms.ModelForm):
#     class Meta:
#         model = Score
#         fields = ['score_number', 'score_select']   #'__all__'
#         widgets = {
#             'score_number': forms.IntegerField(label='Общая оценка', attrs={'class': 'form-input', }),
#             'score_select': forms.Select(attrs={'class': 'form-input', }),
#         }



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', }))
    email = forms.EmailField(label='Адрес эл.почты', widget=forms.EmailInput(attrs={'class': 'form-input', }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', }))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input', }),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input', }),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input', }),
        # }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', }))
