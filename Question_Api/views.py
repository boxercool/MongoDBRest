from django.shortcuts import render
from .models import Question
from .serializers import QuestionWithAnswer
from  rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST', ])
def getquestionWithChoices(request):
    questions = Question.objects.all()
    serializer = QuestionWithAnswer(questions, many=True)
    return Response(serializer.data)
