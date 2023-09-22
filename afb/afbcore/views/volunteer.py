from django.shortcuts import render

# Create your views here.
# some_app/views.py
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from afbcore.forms import VolunteerForm
from afbcore.models import Volunteer
