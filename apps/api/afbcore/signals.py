import logging

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

User = get_user_model()
logger = logging.getLogger(__name__)


"""
  About signals:

  Signal receivers are a safer way to avoid circular references compared to
  direct method calls. When using direct method calls, there is a possibility
  of creating circular references between models, which can lead to memory
  leaks and other issues. By using signals, we can decouple the models and
  avoid direct method calls, reducing the risk of circular references. This
  ensures that the code remains more maintainable and scalable.
"""


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a Profile whenever a User is created.

    Args:
        sender (Model): The model class.
        instance (User): The actual instance being saved.
        created (bool): A boolean; True if a new record was created.
        **kwargs: Arbitrary keyword arguments.
    """
    logger.info(
        f"create_user_profile - instance: {instance}, created: {created}"
    )
    if created:
        # Get the details dictionary from the user instance and if
        # it has keys 'role' and 'phone_number', then pop them out
        # and assign them to the equivalent fields in Profile.
        details = instance.details
        role = details.pop("role", None)
        phone_number = details.pop("phone_number", None)

        # Build the parameters for calling Profile.create. Note that
        # role is a non-nullable field in Profile, so we only include
        # it if it has a value. Otherwise we would get an IntegrityError.
        params = {"user": instance, "phone_number": phone_number}
        if role is not None:
            params["role"] = role

        # Create the profile for the new user
        Profile.objects.create(**params)
