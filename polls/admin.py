from django.contrib import admin

from .models import Question, Choice

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "choice_text", "votes")
    list_filter = ["question"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

