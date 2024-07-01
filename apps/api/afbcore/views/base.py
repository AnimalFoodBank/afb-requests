from rest_framework import viewsets


class UserFilterBaseViewSet(viewsets.ModelViewSet):
    """
    Base viewset that filters the queryset based on a user field.
    The user field should be specified in each subclass.
    """

    user_field = "user"  # default user field, can be overridden in subclasses

    def get_queryset(self):
        """
        This view should return a list of all the objects
        for the currently authenticated user.
        """
        user = self.request.user
        return super().get_queryset().filter(**{self.user_field: user})


class ProfileFilterBaseViewSet(viewsets.ModelViewSet):
    """
    Base viewset that filters the queryset based on a profile field.
    The profile field should be specified in each subclass.
    """

    profile_field = (
        "profile"  # default profile field, can be overridden in subclasses
    )

    def get_queryset(self):
        """
        This view should return a list of all the objects
        for the currently authenticated user's profile.
        """
        user = self.request.user
        return (
            super()
            .get_queryset()
            .filter(**{f"{self.profile_field}__user": user})
        )
