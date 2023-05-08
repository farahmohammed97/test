import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproject.settings')

django.setup()
from testapp.models import Flower
import pytest
from django.conf import settings


@pytest.fixture(name="flower")
def create_flower():
    """Create a merchant instance."""
    return Flower.objects.create(
        name="flower",
        type="plants",
    )


def test_capture_payment_model(flower):
    """Test capture payment model."""
    print(settings.SECRET_KEY)
    assert flower.name == "flower"
    assert flower.type == "plants"
