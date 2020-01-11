from django.urls import path
from final_app import views
from django.contrib.auth import views as auth_views



app_name = 'final_app'
urlpatterns = [  
 path('', views.index, name='index'),
 path('about-page', views.about, name='about'),
 path('contact-page/', views.contact, name='contact'),
 path('course-page', views.courses, name='courses'),
 path('course-details', views.course_details, name='course-details'),
 path('element-page', views.elements, name='elements'),
 
] 