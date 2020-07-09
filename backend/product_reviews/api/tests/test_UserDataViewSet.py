import json
from django.test import TestCase


class TestUserDataViewSet(TestCase):
    check_id = None
    product_id = None

    @classmethod
    def setUpClass(self):
        """
            Posts the product data into the ProductData Model.
        """
        self.content_type = "application/json"
        self.product_payload = {"name": "Olive Oil"}

    def setUp(self):
        """
            SetUp method will be called before executing each test case.
            Validating with Post request by providing valid data
        """
        # Request the Product Id by posting it
        response = self.client.post('/api/productsdata/',
                                    data=json.dumps(self.product_payload),
                                    content_type=self.content_type)
        # Storing ID for further test cases checking
        type(self).product_id = response.json().get('id')

        # Frame payload with all required data
        self.payload = {
            "name": "Abcd",
            "date_of_birth": "2000-02-02",
            "email": "abc@gmail.com",
            "country": "india",
            "city": "hyderabad",
            "likes": "Good Product",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.post('/api/productreviews/',
                                    data=json.dumps(self.payload),
                                    content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('name'), 'Abcd')

        # Storing ID for further test cases checking
        type(self).check_id = response.json().get('user')

    @classmethod
    def tearDownClass(self):
        """
            Resets the default values
        """
        self.check_id = None
        self.product_id = None

    # Checking with Get request
    def test_UserDataViewSet_with_get_request(self):
        """
            Validating UserDataViewSet using get request method
        """
        # Request the data by API call.
        response = self.client.get('/api/userslist/')

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['next'], None)
        self.assertEqual(response.json()['previous'], None)

    # Checking with Get request with Id
    def test_UserDataViewSet_with_get_request_id(self):
        """
            Validating UserDataViewSet using get request method with Id
        """
        # Request the data by API call.
        response = self.client.get('/api/userslist/{}/'.format(
            self.check_id))

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['name'])

    # Checking with Get request with Invalid Id
    def test_UserDataViewSet_with_get_request_Invalid_id(self):
        """
            Validating UserDataViewSet using get request method with
            Invalid Id
        """
        # Request the data by API call.
        response = self.client.get('/api/userslist/{}/'.format(-1))

        # Checking the response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], 'Not found.')
