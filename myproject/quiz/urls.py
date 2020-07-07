from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('solve/<ques_id>', views.solve, name='solve'),
    path('delete/<ques_id>', views.delete, name='delete'),
    path('make_quiz/', views.make_quiz, name='make_quiz'),
    path('contact/', views.contact, name='contact'),
    path('quiz1/', views.quiz1, name='quiz1'),
]
