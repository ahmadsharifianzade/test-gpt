from django import forms

from .models import Form as SurveyForm, Question, Option


class DynamicResponseForm(forms.Form):
    def __init__(self, *args, form_obj: SurveyForm, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_obj = form_obj
        for q in form_obj.questions.all():
            field_name = f"question_{q.id}"
            if q.type == Question.TEXT:
                field = forms.CharField(label=q.text, required=True)
            elif q.type == Question.MULTIPLE_CHOICE:
                choices = [(opt.id, opt.text) for opt in q.options.all()]
                field = forms.ChoiceField(label=q.text, choices=choices, widget=forms.RadioSelect)
            elif q.type == Question.RATING:
                field = forms.IntegerField(label=q.text, min_value=1, max_value=5)
            else:
                continue
            self.fields[field_name] = field
