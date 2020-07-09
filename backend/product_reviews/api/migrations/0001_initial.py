# Generated by Django 2.1.3 on 2020-07-09 06:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('audit_status', models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE'), ('deleted', 'DELETED')], default='active', help_text='Active or InActive', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='On which date field is created')),
                ('modified_on', models.DateTimeField(auto_now=True, help_text='On which date field is modified')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of Product', max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('audit_status', models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE'), ('deleted', 'DELETED')], default='active', help_text='Active or InActive', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='On which date field is created')),
                ('modified_on', models.DateTimeField(auto_now=True, help_text='On which date field is modified')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('likes', models.CharField(help_text='Things that customer likes', max_length=1440, validators=[django.core.validators.MinLengthValidator(3)])),
                ('dislikes', models.CharField(help_text='Things that customer dislikes', max_length=1440, validators=[django.core.validators.MinLengthValidator(3)])),
                ('product_id', models.ForeignKey(help_text='Product Data Id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='productdataid', to='api.ProductData')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('audit_status', models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE'), ('deleted', 'DELETED')], default='active', help_text='Active or InActive', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='On which date field is created')),
                ('modified_on', models.DateTimeField(auto_now=True, help_text='On which date field is modified')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of Customer', max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('date_of_birth', models.DateField(help_text='Date of Birth of the Customer')),
                ('email', models.EmailField(help_text='Email Address of the customer', max_length=100, unique=True)),
                ('country', models.CharField(blank=True, choices=[('afghanistan', 'AFGHANISTAN'), ('albania', 'ALBANIA'), ('algeria', 'ALGERIA'), ('andorra', 'ANDORRA'), ('antigua and barbuda', 'ANTIGUA AND BARBUDA'), ('australia', 'AUSTRALIA'), ('america', 'AMERICA'), ('india', 'INDIA'), ('zimbabwe', 'ZIMBABWE')], default='India', help_text='Country Name', max_length=100, null=True)),
                ('city', models.CharField(blank=True, choices=[('herat', 'HERAT'), ('kabul', 'KABUL'), ('kandahar', 'KANDAHAR'), ('molah', 'MOLAH'), ('wazir akbar khan', 'WAZIR AKBAR KHAN'), ('elbasan', 'ELBASAN'), ('petran', 'PETRAN'), ('pogradec', 'POGRADEC'), ('shkoder', 'SHKODER'), ('tirana', 'TIRANA'), ('ura vajgurore', 'URA VAJGURORE'), ('algiers', 'ALGIERS'), ('oran', 'ORAN'), ('ouargla', 'OUARGLA'), ('oued smar', 'OUED SMAR'), ('tlemcen', 'TLEMCEN'), ('andorra la vella', 'ANDORRA LA VELLA'), ('canillo', 'CANILLO'), ('encamp', 'ENCAMP'), ('sispony', 'SISPONY'), ('soldeu', 'SOLDEU'), ('all saints', 'ALL SAINTS'), ('cassada gardens', 'CASSADA GARDENS'), ('codrington', 'CODRINGTON'), ('old road', 'OLD ROAD'), ('parham', 'PARHAM'), ('woods', 'WOODS'), ('sydney', 'SYDNEY'), ('melbourne', 'MELBOURNE'), ('new york', 'NEW YORK'), ('washington dc', 'WASHINGTON DC'), ('san francisco', 'SAN FRANCISCO'), ('chennai', 'CHENNAI'), ('bangalore', 'BANGALORE'), ('panaji', 'PANAJI'), ('hyderabad', 'HYDERABAD'), ('vijayawada', 'VIJAYAWADA'), ('vizag', 'VIZAG'), ('pune', 'PUNE'), ('mumbai', 'MUMBAI'), ('kolkatta', 'KOLKATTA'), ('delhi', 'DELHI'), ('bulawayo', 'BULAWAYO'), ('chinhoyi', 'CHINHOYI'), ('greendale', 'GREENDALE'), ('gwanda', 'GWANDA'), ('harare', 'HARARE'), ('kwekwe', 'KWEKWE'), ('mufakose', 'MUFAKOSE'), ('mutare', 'MUTARE'), ('victoria falls', 'VICTORIA FALLS')], default='Hyderabad', help_text='Country Name', max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='productreviews',
            name='user',
            field=models.ForeignKey(help_text='User Id for Particular Product', on_delete=django.db.models.deletion.DO_NOTHING, related_name='userproductreview', to='api.UserData'),
        ),
    ]
