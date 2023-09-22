
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import TemplateView, View

from afbcore.models import Client, Manager, Volunteer


class DashboardRouterView(LoginRequiredMixin, View):
    def get(self, request):
        # Route to the specific dashboard based on user type
        if isinstance(request.user, Client):
            # Internal redirect to ClientDashboardView
            return ClientDashboardView.as_view()(request)
        elif isinstance(request.user, Manager):
            # Internal redirect to ManagerDashboardView
            return ManagerDashboardView.as_view()(request)
        elif isinstance(request.user, Volunteer):
            # Internal redirect to VolunteerDashboardView
            return VolunteerDashboardView.as_view()(request)
        else:
            # 404
            raise Http404("Page not found")


class ClientDashboardView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        # Add client-specific dashboard logic here
        return render(request, 'dashboard/client.html')


class ManagerDashboardView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        # Add manager-specific dashboard logic here
        return render(request, 'dashboard/manager.html')


class VolunteerDashboardView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        # Add volunteer-specific dashboard logic here
        return render(request, 'dashboard/volunteer.html')
