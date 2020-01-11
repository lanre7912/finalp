from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
	path('article/', views.article_list, name='list'),
	# path('article/detail/<slug:slug>/', views.article_detail, name='article_detail'),
	path('article/detail/<slug>/', views.article_detail, name='article_detail'),
	path('article-create/', views.article_create, name='create'),
	path('add/<slug>/comment', views.add_comment, name='add_comment'),
	path('comment/<slug>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<slug>/remove/', views.comment_remove, name='comment_remove'),
	path('view_profile_page/', views.view_profile, name='view_profile'),
]