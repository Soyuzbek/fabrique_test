from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from interviews.forms import (
    QuestionForm,
)
from interviews.models import (
    Answer,
    Interview,
    Question,
)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    search_fields = 'text', 'question__text', 'interview__title'


class QuestionInline(admin.TabularInline):
    model = Question
    fields = 'text', 'kind', 'options'
    extra = 0
    form = QuestionForm


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = 'title', 'start_date', 'end_date',
    search_fields = 'title',
    inlines = QuestionInline,

    class Media:
        js = ("js/django_better_admin_arrayfield.min.js", 'js/dynamic_type_field.js')
        css = {"all": ("css/django_better_admin_arrayfield.min.css", 'css/dynamic_type_field.css')}
