from django.contrib import admin

from .models import Form, Question, Option, Response, Answer


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ("text", "type", "form")


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("form", "submitted_at")
    date_hierarchy = "submitted_at"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("response", "question", "text", "option", "rating")
    list_filter = ("question__type",)

