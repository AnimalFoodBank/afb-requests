from django.db import models

from .branch import Branch  # noqa
from .users import User, Profile, Role  # noqa
from .request import Request
from .pet import Pet
from .food_available import FoodAvailable
from .delivery import Delivery, DeliveryRegion

"""
# https://docs.trunk.io/check/ignoring-issues
Branch
Profile
Manager
Client
Volunteer
Pet
HelpRequest
"""
