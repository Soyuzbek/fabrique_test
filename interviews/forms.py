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
            elif len(self.cleaned_data['options']) < 2:
                self.add_error('options', 'Either add more options or choose kind text')
        return self.cleaned_data
