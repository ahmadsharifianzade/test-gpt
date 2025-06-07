from django.urls import path

from . import views

app_name = "crawler"

urlpatterns = [
    path("forms/<int:form_id>/", views.take_form, name="take_form"),
    path("thanks/", views.thanks, name="thanks"),
]
