from quizExam.apiCallQuiz import apiCallQuiz
from django.http.response import HttpResponse
from .apiCallQuiz import apiCallQuiz

# Create your views here.
def QuizSchedule(request):
    return HttpResponse(apiCallQuiz("CS"), content_type='application/json')