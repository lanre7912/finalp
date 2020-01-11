from django.urls import path
from backend import views
from django.contrib.auth import views as auth_views


app_name = 'backend'

urlpatterns = [
	path('login_page/',auth_views.LoginView.as_view(template_name='backend/login.html'), name='login'),
	path('logout_page/', auth_views.LogoutView.as_view(template_name='backend/logout.html'), name='logout'),
	path('register_page/', views.register, name='register'),
	path('password/', views.change_password, name='change_password'),
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('reset_password', views.reset_password, name='reset_password'), 
	path('edit_form_page/', views.edit_form, name='edit_form'),
	
	
]
