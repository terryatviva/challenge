import json
from django.test import TestCase


class TestProductReviewsViewSet(TestCase):
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
        type(self).check_id = response.json().get('id')

    @classmethod
    def tearDownClass(self):
        """
            Resets the default values
        """
        self.check_id = None
        self.product_id = None

    # Checking the POST Valid data for same user with another product Id
    def test_ProductReviewsViewSet_with_post_valid_data(self):
        """
            Validating ProductReviewsViewSet by giving Valid data
            by giving valid new product id for the same user.
        """
        # Request the New Product Id by posting it
        prod_payload = {"name": "Coconut Oil"}
        response = self.client.post('/api/productsdata/',
                                    data=json.dumps(prod_payload),
                                    content_type=self.content_type)

        self.payload['product_id'] = response.json().get('id')

        # Request the data by API call.
        response = self.client.post('/api/productreviews/',
                                    data=json.dumps(self.payload),
                                    content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('name'), 'Abcd')

    # Checking with POST Invalid data
    def test_ProductReviewsViewSet_with_post_Invalid_data(self):
        """
            Validating ProductReviewsViewSet by giving Invalid data
        """
        payload = {
            "name": "1234",
            "date_of_birth": "2030-02-02",
            "email": "abc@gmail.com",
            "country": "india",
            "city": "hyderabad",
            "likes": "Good Product",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": 10000
        }

        # Request the data by API call.
        response = self.client.post('/api/productreviews/',
                                    data=json.dumps(payload),
                                    content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['name'][0],
                         'Name `{0}` must contain atleast one letter'.format(
                             payload.get('name')))

    # Checking with POST Invalid data by modifying Email and Reviews for User
    def test_ProductReviewsViewSet_with_post_Invalid_data_with_email(self):
        """
            Validating ProductReviewsViewSet by giving Invalid data by
            providing Email and Customer Reviews
        """
        payload = {
            "name": "Abcd",
            "date_of_birth": "2000-02-02",
            "email": "abc@gmail.com",
            "country": "india",
            "city": "sydney",
            "likes": "Good Product",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.post('/api/productreviews/',
                                    data=json.dumps(payload),
                                    content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['email']
                         [0], 'Product Review already exists for `{}`.'.format(
                             self.product_id))

    # Checking with Get request
    def test_ProductReviewsViewSet_with_get_request(self):
        """
            Validating ProductReviewsViewSet using get request method
        """
        # Request the data by API call.
        response = self.client.get('/api/productreviews/')

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['next'], None)
        self.assertEqual(response.json()['previous'], None)

    # Checking with Get request with Id
    def test_ProductReviewsViewSet_with_get_request_id(self):
        """
            Validating ProductReviewsViewSet using get request method with Id
        """
        # Request the data by API call.
        response = self.client.get('/api/productreviews/{}/'.format(
            self.check_id))

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['next'], None)
        self.assertEqual(response.json()['previous'], None)

    # Checking with Get request with Invalid Id
    def test_ProductReviewsViewSet_with_get_request_Invalid_id(self):
        """
            Validating ProductReviewsViewSet using get request method with
            Invalid Id
        """
        # Request the data by API call.
        response = self.client.get('/api/productreviews/{}/'.format(-1))

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['id'],
                         'User Id `-1` must be an Positive Integer.')

    # Checking with Put Request with valid data
    def test_ProductReviewsViewSet_with_put_valid_data(self):
        """
            Validating ProductReviewsViewSet by giving Valid data.
        """
        payload = {
            "name": "Abcd",
            "date_of_birth": "2000-02-02",
            "email": "abc@gmail.com",
            "country": "india",
            "city": "hyderabad",
            "likes": "Good Products",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.put(
            '/api/productreviews/{}/'.format(self.check_id),
            data=json.dumps(payload), content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Abcd')

    # Checking with Put Request with Invalid data Email
    def test_ProductReviewsViewSet_with_put_Invalid_data_email(self):
        """
            Validating ProductReviewsViewSet by giving InValid data.
        """
        payload = {
            "name": "Abcd",
            "date_of_birth": "2000-02-02",
            "email": "abca@gmail.com",
            "country": "india",
            "city": "hyderabad",
            "likes": "Good Products",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.put(
            '/api/productreviews/{}/'.format(self.check_id),
            data=json.dumps(payload), content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['email'][0],
                         'Email Address `{}` not exists'.format(
                             payload.get('email')))

    # Checking with Put Request with Invalid data Name
    def test_ProductReviewsViewSet_with_put_Invalid_name(self):
        """
            Validating ProductReviewsViewSet by giving InValid Name.
        """
        payload = {
            "name": "AbCd",
            "date_of_birth": "2000-02-02",
            "email": "abc@gmail.com",
            "country": "india",
            "city": "hyderabad",
            "likes": "Good Products",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.put(
            '/api/productreviews/{}/'.format(self.check_id),
            data=json.dumps(payload), content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['name'][0],
                         'Name `{}` cannot be editable'.format(
                             payload.get('name')))

    # Checking with Put Request with Invalid data Date of Birth
    def test_ProductReviewsViewSet_with_put_Invalid_dob(self):
        """
            Validating ProductReviewsViewSet by giving InValid Date of Birth.
        """
        payload = {
            "name": "Abcd",
            "date_of_birth": "2001-02-02",
            "email": "abc@gmail.com",
            "country": "india",
            "city": "hyderabad",
            "likes": "Good Products",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.put(
            '/api/productreviews/{}/'.format(self.check_id),
            data=json.dumps(payload), content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['date_of_birth'][0],
                         'Date of Birth `{}` cannot be editable'.format(
                             payload.get('date_of_birth')))

    # Checking with Put Request with Invalid data Email
    def test_ProductReviewsViewSet_with_put_Invalid_email(self):
        """
            Validating ProductReviewsViewSet by giving InValid Email.
        """
        payload = {
            "name": "Abcd",
            "date_of_birth": "2000-02-02",
            "email": "abC@gmail.com",
            "country": "india",
            "city": "hyderabad",
            "likes": "Good Products",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.put(
            '/api/productreviews/{}/'.format(self.check_id),
            data=json.dumps(payload), content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['email'][0],
                         'Email `{}` cannot be editable'.format(
                             payload.get('email')))

    # Checking with Put Request with Invalid data Country
    def test_ProductReviewsViewSet_with_put_Invalid_country(self):
        """
            Validating ProductReviewsViewSet by giving InValid Country.
        """
        payload = {
            "name": "Abcd",
            "date_of_birth": "2000-02-02",
            "email": "abc@gmail.com",
            "country": "australia",
            "city": "sydney",
            "likes": "Good Products",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.put(
            '/api/productreviews/{}/'.format(self.check_id),
            data=json.dumps(payload), content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['country'][0],
                         'Country `{}` cannot be editable'.format(
                             payload.get('country')))

    # Checking with Put Request with Invalid data City
    def test_ProductReviewsViewSet_with_put_Invalid_city(self):
        """
            Validating ProductReviewsViewSet by giving InValid City.
        """
        payload = {
            "name": "Abcd",
            "date_of_birth": "2000-02-02",
            "email": "abc@gmail.com",
            "country": "india",
            "city": "panaji",
            "likes": "Good Products",
            "dislikes": "Proper Nutrition facts not present",
            "product_id": self.product_id
        }

        # Request the data by API call.
        response = self.client.put(
            '/api/productreviews/{}/'.format(self.check_id),
            data=json.dumps(payload), content_type=self.content_type)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['city'][0],
                         'City `{}` cannot be editable'.format(
                             payload.get('city')))

