# PRODUCT REVIEWS

### Product Reviews Unit Tests

    This directory contains tests for the Product Reviews. It has a combination of Django TestCases (which will create a test database before running each test).

# Running Unit Tests

## Install prerequisites

    pip3 install coverage

## By Activating Virtual Environment or in Docker Container
    
- To run all Unit tests

    `coverage run manage.py test`

- To run single unit test module

    `coverage run manage.py test api.tests.test_ProductReviewsViewSet`

- To run single test in unit test module

    `coverage run manage.py test api.tests.test_ProductReviewsViewSet.TestProductReviewsViewSet.test_ProductReviewsViewSet_with_get_request`

## Coverage report

- To check Code Coverage

    `coverage report -m --omit=manage.py`
