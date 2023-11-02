from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from afbcore.serializers import UserSerializer

User = get_user_model()


# class MyLoginView(LoginView):
#     template_name = "afbcore/login.html"
#     success_url = reverse_lazy("afbcore:dashboard")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
