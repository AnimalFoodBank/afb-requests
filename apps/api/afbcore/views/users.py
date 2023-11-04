from afbcore.serializers import RegisterUserSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """
    https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
    """

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def current_user(self, request):
        serializer = self.get_serializer(request.user, context={"request": request})
        return Response(serializer.data)

    @api_view(["POST"])
    def register(request):
        """
        Register a new user.
        """
        serializer = UserSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
