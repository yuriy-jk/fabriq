# Generated by Django 3.2.7 on 2021-09-11 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_auto_20210910_2024"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.IntegerField()),
                ("text", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Ask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("text", "Only_text_answer"),
                            ("one_choice", "Answer with one choice"),
                            ("many_choice", "Answer with many choices"),
                        ],
                        max_length=64,
                        verbose_name="ask_type",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="quiz",
            name="name",
        ),
        migrations.AddField(
            model_name="quiz",
            name="title",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name="Asks",
        ),
        migrations.AddField(
            model_name="ask",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quiz_asks",
                to="quiz.quiz",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="ask",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ask",
                to="quiz.ask",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quiz",
                to="quiz.quiz",
            ),
        ),
    ]
