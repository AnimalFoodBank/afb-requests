"""
URL configuration for afb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from afbcore.views import users

router = routers.DefaultRouter()
router.register(r"users", users.UserViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path("login/", views.MyLoginView.as_view(), name="login"),
    # Part of django-tailwind
    # See https://django-tailwind.readthedocs.io/en/latest/installation.html#configuration
    path("__reload__/", include("django_browser_reload.urls")),
]
