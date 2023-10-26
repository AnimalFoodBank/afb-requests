from django.shortcuts import render

# Create your views here.
# some_app/views.py
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from afbcore.forms import ClientSignupForm
from afbcore.models import Client


class AboutView(TemplateView):
    template_name = "about.html"


class DashboardView(TemplateView):
    template_name = "dashboard/client.html"


class ClientSignupFormView(FormView):
    template_name = "afbcore/client_signup_form.html"
    form_class = ClientSignupForm


class ClientCreateView(CreateView):
    model = Client
    fields = ["first_name", "last_name", "email", "address", "phone_number"]


class ClientRequestView(TemplateView):
    template_name = "afbcore/client_request.html"
