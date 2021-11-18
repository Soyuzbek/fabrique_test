# Generated by Django 3.2.5 on 2021-11-18 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'interview',
                'verbose_name_plural': 'interviews',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='text')),
                ('kind', models.CharField(choices=[('text', 'text'), ('choice', 'choice'), ('multiple', 'multiple choice')], default='text', max_length=45, verbose_name='kind')),
                ('options', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('interview', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='interviews.interview')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interviews.question')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'answer',
                'verbose_name_plural': 'answers',
            },
        ),
    ]