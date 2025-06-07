from django.shortcuts import get_object_or_404, redirect, render

from .forms import DynamicResponseForm
from .models import Answer, Form as SurveyForm, Question, Response


def take_form(request, form_id):
    form_obj = get_object_or_404(SurveyForm.objects.prefetch_related("questions__options"), pk=form_id)
    if request.method == "POST":
        form = DynamicResponseForm(request.POST, form_obj=form_obj)
        if form.is_valid():
            response = Response.objects.create(form=form_obj)
            for q in form_obj.questions.all():
                key = f"question_{q.id}"
                data = form.cleaned_data.get(key)
                if q.type == Question.TEXT:
                    Answer.objects.create(response=response, question=q, text=data)
                elif q.type == Question.MULTIPLE_CHOICE:
                    Answer.objects.create(response=response, question=q, option_id=int(data))
                elif q.type == Question.RATING:
                    Answer.objects.create(response=response, question=q, rating=int(data))
            return redirect("crawler:thanks")
    else:
        form = DynamicResponseForm(form_obj=form_obj)
    return render(request, "crawler/form.html", {"form": form, "form_obj": form_obj})


def thanks(request):
    return render(request, "crawler/thanks.html")
