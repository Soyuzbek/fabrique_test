from django.db.models import TextChoices


class Kind(TextChoices):
    TEXT = 'text', 'text'
    CHOICE = 'choice', 'choice'
    MULTIPLE = 'multiple', 'multiple choice'
