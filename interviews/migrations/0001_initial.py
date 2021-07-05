# Generated by Django 3.2.5 on 2021-07-05 13:06

from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('options', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interviews.interview')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
        ),
    ]