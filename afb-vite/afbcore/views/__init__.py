from .client import *
from .dashboard import (
    ClientDashboardView,
    DashboardRouterView,
    ManagerDashboardView,
    VolunteerDashboardView,
)

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class MyLoginView(LoginView):
    template_name = "afbcore/login.html"
    success_url = reverse_lazy("afbcore:dashboard")
