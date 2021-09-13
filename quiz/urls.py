from django.urls import path

from quiz.views import ActiveQuizList, StartQuiz, UserQuiz

urlpatterns = [
    path("active_quiz/", ActiveQuizList.as_view()),
    path("start_quiz/", StartQuiz.as_view()),
    path("user_quiz/", UserQuiz.as_view()),
]
