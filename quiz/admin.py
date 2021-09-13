from django.contrib import admin

from quiz.models import Quiz, Ask


# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "start_date", "finish_date"]


@admin.register(Ask)
class AsksAdmin(admin.ModelAdmin):
    list_display = ["quiz", "text", "type"]
