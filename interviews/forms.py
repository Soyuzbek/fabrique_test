from django import forms

from interviews.choices import (
   Kind,
)
from interviews.models import (
    Question,
)


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = 'text', 'kind', 'options'

    def clean(self):
        if self.cleaned_data['kind'] == Kind.TEXT:
            self.cleaned_data['options'] = None
        else:
            if not self.cleaned_data['options']:
                self.add_error('options', 'Options is required when choice or multiple choice selected')
        return self.cleaned_data
