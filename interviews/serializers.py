from rest_framework import serializers as srz

from interviews.models import (
    Interview,
    Question,
)


class QuestionSerializer(srz.ModelSerializer):
    class Meta:
        model = Question
        fields = 'id', 'text', 'kind', 'options'


class InterviewSerializer(srz.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True)

    class Meta:
        model = Interview
        fields = 'id', 'title', 'description', 'questions'
