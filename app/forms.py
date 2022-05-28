import django
from django import forms


from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('userId','title', 'body')

        widgets = {
            #'userId': forms.Select(attrs={'class': 'form-control'}),
            'userId': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'meno', 'type':'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }