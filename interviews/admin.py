from django.contrib import admin

from interviews.forms import (
    QuestionForm,
)
from interviews.models import (
    Interview,
    Question,
)


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
