import json
from django.test import TestCase


class TestProductsDataViewSet(TestCase):
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

        # Checking the response
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('name'), 'Olive Oil')

        # Storing ID for further test cases checking
        type(self).product_id = response.json().get('id')

    @classmethod
    def tearDownClass(self):
        """
            Resets the default values
        """
        self.product_id = None

    # Checking with POST Invalid data
    def test_ProductsDataViewSet_with_post_Invalid_data(self):
        """
            Validating ProductsDataViewSet by giving Invalid data
        """
        payload = {
            "name": "1234"
        }

        # Request the data by API call.
        response = self.client.post('/api/productsdata/',
                                    data=json.dumps(payload),
                                    content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['name'][0],
                         'Name `{0}` must contain atleast one letter'.format(
                             payload.get('name')))

    # Checking with Get request
    def test_ProductsDataViewSet_with_get_request(self):
        """
            Validating ProductsDataViewSet using get request method
        """
        # Request the data by API call.
        response = self.client.get('/api/productsdata/')

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['next'], None)
        self.assertEqual(response.json()['previous'], None)

    # Checking with Get request with Id
    def test_ProductsDataViewSet_with_get_request_id(self):
        """
            Validating ProductsDataViewSet using get request method with Id
        """
        # Request the data by API call.
        response = self.client.get('/api/productsdata/{}/'.format(
            self.product_id))

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['name'])

    # Checking with Get request with Invalid Id
    def test_ProductsDataViewSet_with_get_request_Invalid_id(self):
        """
            Validating ProductsDataViewSet using get request method with
            Invalid Id
        """
        # Request the data by API call.
        response = self.client.get('/api/productsdata/{}/'.format(-1))

        # Checking the response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], 'Not found.')
