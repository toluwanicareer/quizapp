from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from .models import Quiz, Question, Answers
from django.http import JsonResponse

# Create your views here.

class Home(ListView):
    model=Quiz
    queryset = Quiz.objects.all()
    context_object_name = 'quizs'
    template_name = 'index.html'

class NextQuizsMixin:

    def get_context_data(self, **kwargs):
        context=super(NextQuizsMixin, self).get_context_data(**kwargs)
        context['next_quizs']=Quiz.objects.all()[0:5]
        return context

class QuizDetail(NextQuizsMixin, DetailView):
    model=Quiz
    context_object_name = 'quiz'
    template_name = 'quiz.html'
    slug_field = 'slug'



class Questions(NextQuizsMixin,DetailView):
    model = Quiz
    context_object_name ='quiz'
    template_name = 'question.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context=super(Questions, self).get_context_data(**kwargs)
        context['questions']=Question.objects.filter(quiz=self.object)
        context['no_of_questions']=context['questions'].__len__()
        return context

class HandleResponse(View):

    def get(self,request, *args, **kwargs):
        score=request.GET.get('score')
        quiz_id=request.GET.get('quiz_id')
        answers=Answers.objects.filter(quiz_id=quiz_id)
        quiz=Quiz.objects.get(id=quiz_id)
        for answer in answers:
            if answer.min_score < int(score) and answer.max_score > int(score) :
                result= answer
        return JsonResponse({'answer_id':result.id, 'quiz_id':quiz_id, 'quiz_slug':quiz.slug})


class ShowAnswer(NextQuizsMixin,DetailView):
    model = Answers
    template_name = 'answer.html'
    context_object_name = 'answer'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context=super(ShowAnswer, self).get_context_data(**kwargs)
        context['quiz']=self.object.quiz
        return context









