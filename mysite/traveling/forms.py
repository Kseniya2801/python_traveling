from django import forms
from .models import*
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Traveling
        fields = ['title', 'slug', 'content','photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'contant': forms.Textarea(attrs={'cols': 60, 'rows':10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Длина заголовка превышает 20 символов')
        return title
