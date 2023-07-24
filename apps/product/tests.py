import pytest


pytestmark = pytest.mark.django_db


class TestHomeView:
    """
    Test class for TestHomeView and API's.
    """
    endpoint = '/'

    def test_get_home(self, api_client):
        """
        Test method to assert the validity and persistence of endpoint with proper responses.
        """
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
