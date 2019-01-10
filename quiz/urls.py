from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('quiz/handle_response', views.HandleResponse.as_view()),
    path('quiz/<str:slug>', views.QuizDetail.as_view(), name='quiz-detail'),
    path('quiz/<str:slug>/questions', views.Questions.as_view()),
    path('quiz/<str:slug>/<int:id>', views.ShowAnswer.as_view()),

]