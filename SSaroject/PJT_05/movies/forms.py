from .models import Movie, Comment
from django import forms


# class MovieForm(forms.ModelForm):
# 	class Meta:
# 		model = Movie
# 		fields = ('title', 'content',)

# class CommentForm(forms.ModelForm):
# 	class Meta:
# 		model = Comment
# 		fields = '__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('user',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            'user',
            'movie',
        )
