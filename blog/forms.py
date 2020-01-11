from django import forms
from blog import models
from .models import Article, Comment


class CreateArticle(forms.ModelForm):
	class Meta():
		model = models.Article
		fields = ('title', 'content', 'slug', 'image', 'author')

class CommentForm(forms.ModelForm):
	class Meta():
		model = models.Comment
		fields = ('author', 'content')
