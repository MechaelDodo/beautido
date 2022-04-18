from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddGirlForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Girl
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']   #'__all__'
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
