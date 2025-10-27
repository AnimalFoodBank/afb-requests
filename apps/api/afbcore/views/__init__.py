# views/__init__.py

"""
This module contains the views for the AFB Core API
application.

The views are responsible for handling HTTP requests and
returning HTTP responses.
Each view corresponds to one or more URL patterns, and
is responsible for handling all HTTP methods (GET, POST,
PUT, DELETE, etc.) that are allowed for that URL pattern.

This module also includes any helper functions or
classes that are used exclusively by the views in this
module.
"""

from .branch_viewset import BranchViewSet  # noqa: F401
from .food_request_view import FoodRequestViewSet  # noqa: F401
from .pet_viewset import PetViewSet  # noqa: F401
from .profile_viewset import ProfileViewSet  # noqa: F401
from .user_view import CurrentUserAPIView, RegisterUserAPIView  # noqa: F401
