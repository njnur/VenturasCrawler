import pytest


@pytest.fixture
def api_client():
    """
    Fixture for DRF's APIClient object
    """
    from rest_framework.test import APIClient
    return APIClient
