from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    TEXT = "TEXT"
    MULTIPLE_CHOICE = "MC"
    RATING = "RATING"

    QUESTION_TYPES = [
        (TEXT, "Short answer"),
        (MULTIPLE_CHOICE, "Multiple choice"),
        (RATING, "Rating"),
    ]

    form = models.ForeignKey(Form, related_name="questions", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=QUESTION_TYPES)

    def __str__(self) -> str:
        return self.text


class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text


class Response(models.Model):
    form = models.ForeignKey(Form, related_name="responses", on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    response = models.ForeignKey(Response, related_name="answers", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

