import json
import logging

from rest_framework import viewsets, serializers
from django.core.serializers.json import DjangoJSONEncoder

from api.services.utils import check_positivenum
from api.models import ProductReviews, UserData, ProductData
from api.restful.serializers import (ProductReviewsSerializer,
                                     UserDataSerializer,
                                     ProductDataSerializer)

# Get an instance of a logger
logger = logging.getLogger(__name__)


def paginating_queryset(self, queryset, request):
        """
            1. Paginate the request and queryset.
            2. Logs the information into log file.
        """
        results = self.paginator.paginate_queryset(queryset, request)
        response = self.paginator.get_paginated_response(
            json.dumps(results, cls=DjangoJSONEncoder)
        )
        response.data['results'] = json.loads(response.data['results'])
        return response


class UserDataViewSet(viewsets.ModelViewSet):
    """
        Gets the list of Users Data
    """
    http_method_names = ['get']
    queryset = UserData.objects.all().order_by('name')
    serializer_class = UserDataSerializer


class ProductReviewsViewSet(viewsets.ModelViewSet):
    """
        Invokes ModelViewSet to perform all CRUD operations.
    """
    queryset = ProductReviews.objects.all()
    serializer_class = ProductReviewsSerializer
    # pagination_class = LimitOffsetPagination

    def list(self, request):
        """
            Lists all the product reviews.
        """
        query = self.queryset.values()
        response = paginating_queryset(self, query, request)
        return response

    def retrieve(self, request, pk=None, tenant_pk=None):
        """
            Retrieve specific product details review
        """
        # Checks whether the given pk is positive or not.
        if not (check_positivenum(pk)):
            raise_value = {"id": "User Id `{0}` must be an Positive Integer."
                           .format(pk)}
            logger.error("ID error is : " + str(raise_value))
            raise serializers.ValidationError(raise_value)
        query = self.queryset.filter(id=pk).values()
        response = paginating_queryset(self, query, request)
        return response


class ProductsDataViewSet(viewsets.ModelViewSet):
    """
        Gets the list of products data
    """
    http_method_names = ['get', 'post']
    queryset = ProductData.objects.all().order_by('name')
    serializer_class = ProductDataSerializer
