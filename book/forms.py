from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','description','publish_year']
        widgets={
            "title":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Write Book Title...",
                }
            ),
            "author":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Write Book Author...",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),
            "publish_year":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Write Publish Year",
                }
            ),

        }