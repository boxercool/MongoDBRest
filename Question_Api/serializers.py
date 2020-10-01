
from .models import  Choice,Question
from rest_framework import  serializers

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'votes', 'choice_text',)



class QuestionWithAnswer(serializers.ModelSerializer):
    question = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date','question')