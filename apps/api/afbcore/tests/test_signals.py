# Test setup

from unittest.mock import patch

import pytest
from afbcore.models.users.profile import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user_model():
    return get_user_model()


@pytest.fixture
def profile_model():
    return Profile


@pytest.mark.django_db
def test_create_user_profile_signal(user_model, profile_model):
    # Test case 1: User creation with default profile creation
    user = user_model.objects.create_user(
        "test21@example.com", "testuser", "password"
    )
    assert Profile.objects.filter(user=user).exists()

    # Test case 2: User creation without default profile creation
    with patch("afbcore.signals.create_user_profile") as mock_signals:
        user = user_model.objects.create_user(
            "test22@example.com", "testuser", "password"
        )
        mock_signals.assert_not_called()

    # Test case 3: Profile creation with existing user
    user = user_model.objects.create_user(
        "test23@example.com", "testuser", "password"
    )
    profile = profile_model.objects.create(user=user)
    assert profile.user == user

    # Test case 4: Profile creation with non-existing user
    with pytest.raises(User.DoesNotExist):
        profile_model.objects.create(user=user_model.objects.get(id=9999))
