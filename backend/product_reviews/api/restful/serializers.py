
import logging

from datetime import datetime
from rest_framework import serializers
from django.core.validators import (MinLengthValidator)

from api.models import ProductReviews, UserData, ProductData
from api.services.utils import (check_alpha_exists, get_countries,
                                check_city_exists)

COUNTRIES, CITIES = get_countries()

# Get an instance of a logger
logger = logging.getLogger(__name__)


class UserDataSerializer(serializers.ModelSerializer):
    """
        UserDataSerializer inherits ModelSerializer. This ModelSerializer
        will perform all necessary operations like insert, update, select,
        delete.
    """

    class Meta:
        model = UserData
        exclude = ('audit_status',)


class ProductReviewsSerializer(serializers.ModelSerializer):

    def validate_name(self, data):
        # Validates the name exists with One Letter
        if not check_alpha_exists(data):
            msg = ("Name `{0}` must contain atleast one letter".format(data))
            logger.error(msg)
            raise serializers.ValidationError(msg)
        return data

    def validate_email(self, data):
        # Checks whether Email exists or not.
        product_id = self.initial_data.get('product_id')
        user_id = UserData.objects.filter(email__iexact=data)
        # Checks whether the User have already reviewed for specific product
        if (self.context.get('request') and
            self.context.get('request').method in ['POST'] and
            user_id and ProductReviews.objects.filter(
                        product_id=product_id, user=user_id[0])):
            msg = "Product Review already exists for `{}`.".format(product_id)
            logger.error(msg)
            raise serializers.ValidationError(msg)
        # Checks whether the Email Address exists or not for PUT request
        if (self.context.get('request') and
            self.context.get('request').method in ['PUT'] and
                not user_id):
            msg = "Email Address `{}` not exists".format(data)
            logger.error(msg)
            raise serializers.ValidationError(msg)
        return data

    def validate_date_of_birth(self, data):
        # Checks whether the date of birth correct or not.
        if str(data) > str(datetime.now().date()):
            msg = "Date of Birth `{0}` exceeds than Current Date `{1}`".format(
                data, str(datetime.now().date()))
            logger.error(msg)
            raise serializers.ValidationError(msg)
        return data

    def validate_city(self, data):
        # Checks whether the city is in specified country or not.
        if not check_city_exists(self.initial_data.get('country'), data):
            msg = "City `{0}` not exists in selected Country `{1}`.".format(
                data, self.initial_data.get('country'))
            logger.error(msg)
            raise serializers.ValidationError(msg)
        return data

    def validate(self, data):
        # Checks for not to modify the Customer Name, DOB, Email, Country, City
        product_id = data.get('product_id')
        user_id = UserData.objects.filter(email__iexact=data.get('email'))
        if user_id:
            prod_review = ProductReviews.objects.filter(
                    product_id=product_id, user=user_id[0])
            if prod_review:
                if user_id[0].name != data.get('name'):
                    msg = {"name": "Name `{}` cannot be editable".format(
                        data.get('name'))}
                    logger.error(msg)
                    raise serializers.ValidationError(msg)
                if user_id[0].date_of_birth != data.get('date_of_birth'):
                    msg = {"date_of_birth":
                           "Date of Birth `{}` cannot be editable".format(
                            data.get('date_of_birth'))}
                    logger.error(msg)
                    raise serializers.ValidationError(msg)
                if user_id[0].email != data.get('email'):
                    msg = {"email": "Email `{}` cannot be editable".format(
                        data.get('email'))}
                    logger.error(msg)
                    raise serializers.ValidationError(msg)
                if user_id[0].country != data.get('country'):
                    msg = {"country": "Country `{}` cannot be editable".format(
                        data.get('country'))}
                    logger.error(msg)
                    raise serializers.ValidationError(msg)
                if user_id[0].city != data.get('city'):
                    msg = {"city": "City `{}` cannot be editable".format(
                        data.get('city'))}
                    logger.error(msg)
                    raise serializers.ValidationError(msg)
        return data

    name = serializers.CharField(
        validators=[MinLengthValidator(3)], required=True,
        max_length=50, help_text='Name of the Customer')
    date_of_birth = serializers.DateField(
        required=True, help_text='Date of Birth of the Customer')
    email = serializers.EmailField(
        max_length=100, help_text='Email Address of the customer')
    country = serializers.ChoiceField(
        choices=COUNTRIES,
        required=True, help_text='Customer Country')
    city = serializers.ChoiceField(
        choices=CITIES,
        required=True, help_text='Customer City')

    class Meta:
        model = ProductReviews
        read_only_fields = ('user',)
        exclude = ('audit_status',)

    def create(self, validated_data):
        # Pops the user data and populates its field to UserData Model
        name = validated_data.pop('name')
        date_of_birth = validated_data.pop('date_of_birth')
        email = validated_data.pop('email')
        country = validated_data.pop('country')
        city = validated_data.pop('city')
        user_data_obj = {
            "name": name,
            "date_of_birth": date_of_birth,
            "email": email,
            "country": country,
            "city": city
        }
        # Checks User Email exists or not and then updates for product
        user_data = UserData.objects.filter(email__iexact=email)
        if user_data:
            user_data = user_data[0]
        else:
            user_data = UserData.objects.create(**user_data_obj)
        validated_data['user'] = user_data
        # Populates Product data in ProductReviews Model
        product_review = ProductReviews.objects.create(**validated_data)
        product_review.name = name
        product_review.date_of_birth = date_of_birth
        product_review.email = email
        product_review.country = country
        product_review.city = city
        return product_review

    def update(self, instance, validated_data):
        # Updates the Customer likes and dislikes for specific instance
        instance.likes = validated_data.get('likes')
        instance.dislikes = validated_data.get('dislikes')
        instance.save()
        return validated_data


class ProductDataSerializer(serializers.ModelSerializer):

    def validate_name(self, data):
        # Validates the name exists with One Letter
        if not check_alpha_exists(data):
            msg = ("Name `{0}` must contain atleast one letter".format(data))
            logger.error(msg)
            raise serializers.ValidationError(msg)
        return data

    class Meta:
        model = ProductData
        exclude = ('audit_status', 'created_on', 'modified_on')
