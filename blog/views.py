from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateArticle
from .models import Article, Comment
from . import forms
from blog.forms import CommentForm, CreateArticle
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):
	articles = Article.objects.all().order_by('-date')
	return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, slug):
	article = Article.objects.get(slug=slug)
	return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def add_comment(request, slug):
	article = get_object_or_404(Article, slug=slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			Comment.article = article
			comment.save()
			return redirect('blog:article_detail', slug=article.slug)
	else:
		form = CommentForm()
	return render(request, 'blog/add_comment.html', {'form': form})

@login_required
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('blog:list')
	else:
		form = forms.CreateArticle()		
	return render(request, 'blog/article_create.html', {'form': form})

@login_required
def comment_approve(request, slug):
	comment = get_object_or_404(Comment, slug=slug)
	comment.approve()
	return redirect('article_detail', slug=comment.article.slug)

@login_required
def comment_remove(request, slug):
	comment = get_object_or_404(Comment, slug=slug)
	comment.delete()
	return redirect('article_detail', slug=comment.article.slug)				

def view_profile(request): 
	return render(request, 'blog/view_profile.html', {'profile':request.user})
