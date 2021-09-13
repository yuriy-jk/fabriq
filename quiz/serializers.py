from rest_framework import serializers

from quiz.models import Quiz, Ask, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("id", "title", "description")


class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ask
        fields = ("id", "quiz", "type", "text")


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('ask', 'text')


class UserQuizSerializer(serializers.Serializer):
    quiz = QuizSerializer()
    answers = AnswerListSerializer(many=True)
