from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

from interviews.choices import (
    Kind,
)


class Interview(models.Model):
    title = models.CharField('title', max_length=255)
    start_date = models.DateTimeField('start date', auto_now_add=True)
    end_date = models.DateTimeField('end date')
    description = models.TextField('description', null=True, blank=True)

    class Meta:
        verbose_name = 'interview'
        verbose_name_plural = 'interviews'

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField('text', max_length=255)
    kind = models.CharField('kind', max_length=45, choices=Kind.choices, default=Kind.TEXT)
    options = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    interview = models.ForeignKey(Interview, models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=500, null=True, blank=True)
    multiple = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    interview = models.ForeignKey(Interview, models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Question, models.CASCADE)
    user = models.ForeignKey('accounts.User', models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'

    def __str__(self):
        if self.text:
            return self.text
        return super().__str__()
