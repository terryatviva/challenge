from __future__ import unicode_literals

from django.db import models
from django.core.validators import (MinLengthValidator)

from api.services.constants import Variables
from api.services.utils import get_countries

COUNTRIES, CITIES = get_countries()


class Audit(models.Model):
    # Audit Details
    """
    An abstract base class model that provides self updating ``created``
    and ``modified`` fields.
    """
    audit_status = models.CharField(
        choices=Variables.audit_status, max_length=10, default='active',
        help_text='Active or InActive')
    created_on = models.DateTimeField(
        auto_now_add=True, help_text='On which date field is created')
    modified_on = models.DateTimeField(
        auto_now=True, help_text='On which date field is modified')

    class Meta:
        abstract = True


class ProductData(Audit):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)],
                            help_text='Name of Product')


class UserData(Audit):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)],
                            help_text='Name of Customer')
    date_of_birth = models.DateField(
        help_text='Date of Birth of the Customer')
    email = models.EmailField(max_length=100, unique=True,
                              help_text='Email Address of the customer')
    country = models.CharField(
        choices=COUNTRIES, max_length=100, default="India", null=True,
        blank=True, help_text='Country Name')
    city = models.CharField(
        choices=CITIES, max_length=100, default="Hyderabad", null=True,
        blank=True, help_text='Country Name')


class ProductReviews(Audit):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserData, models.DO_NOTHING,
                             related_name="userproductreview",
                             help_text='User Id for Particular Product')
    product_id = models.ForeignKey(
        ProductData, models.DO_NOTHING, related_name="productdataid",
        help_text='Product Data Id')
    likes = models.CharField(max_length=1440,
                             validators=[MinLengthValidator(3)],
                             help_text='Things that customer likes')
    dislikes = models.CharField(max_length=1440,
                                validators=[MinLengthValidator(3)],
                                help_text='Things that customer dislikes')
