import datetime

import pytz
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Quiz, Ask, Answer
from quiz.serializers import QuizSerializer, AskSerializer, \
    AnswerSerializer, UserQuizSerializer, AnswerListSerializer

# Create your views here.

moscow = pytz.timezone("Europe/Moscow")


class ActiveQuizList(ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        now = datetime.datetime.now(tz=moscow)
        queryset = Quiz.objects.all()
        res = [x for x in queryset if x.start_date < now < x.finish_date]
        return res


class StartQuiz(APIView):
    def get(self, request):
        quiz = self.request.data["quiz_id"]
        queryset = Ask.objects.filter(quiz_id=quiz)
        serializer = AskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        quiz = Quiz.objects.get(id=self.request.data["quiz"])
        ask = Ask.objects.get(id=self.request.data["ask"])
        serializer = AnswerSerializer(data=self.request.data)
        if serializer.is_valid():
            Answer.objects.create(
                user=data["user"], quiz=quiz, ask=ask, text=data["text"]
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserQuiz(APIView):
    def get(self, request):
        user = self.request.data["user"]
        answer_queryset = Answer.objects.filter(user=user)
        quiz_list = [i.quiz_id for i in answer_queryset]
        user_quiz = set(quiz_list)
        res = []
        for quiz in user_quiz:
            quiz = Quiz.objects.get(id=quiz)
            answers_query = Answer.objects.filter(quiz=quiz).filter(user=user)
            answers_serializer = AnswerListSerializer(answers_query, many=True)
            result = UserQuizSerializer(data={'quiz': {'quiz_id': quiz.id, 'quiz_title': quiz.title},
                                              'answers': answers_serializer.data})
            res.append(result.initial_data)

        return Response(res, status=status.HTTP_201_CREATED)
