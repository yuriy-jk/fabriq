from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

ASK_TYPE = (
    ("text", _("Only_text_answer")),
    ("one_choice", _("Answer with one choice")),
    ("many_choice", _("Answer with many choices")),
)


class Quiz(models.Model):
    title = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()


class Ask(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name="quiz_asks", on_delete=models.CASCADE, db_index=True
    )
    text = models.TextField(blank=False)
    type = models.CharField(
        max_length=64,
        verbose_name="ask_type",
        choices=ASK_TYPE,
    )


class Answer(models.Model):
    user = models.IntegerField()
    quiz = models.ForeignKey(
        Quiz, related_name="quiz", on_delete=models.CASCADE, db_index=True
    )
    ask = models.OneToOneField(
        Ask, related_name="ask", on_delete=models.CASCADE, db_index=True
    )
    text = models.TextField(blank=True)
