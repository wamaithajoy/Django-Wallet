# Generated by Django 4.0.6 on 2022-08-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywallet', '0002_account_currency_receipts_customer_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_pictures/'),
        ),
    ]
