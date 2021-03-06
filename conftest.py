import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """User instance from default django user model"""
    yield django_user_model.objects.create_user(email='a11@a.pl', fullname='Ala', password='testPass123')
