from .models import Book, Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)
        label = {
            'content' : '리뷰 작성'
        }