import pytest


pytestmark = pytest.mark.django_db


class TestProductView:
    """
    Test class for TestAccountViewSet and API's.
    This class comprises several methods that includes both positive and negative test suits.
    """
    endpoint = '/api/events/'

    def test_get_endpoint(self, api_client):
        """
        Test method to assert the validity and persistence of endpoint with proper responses.
        """
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
