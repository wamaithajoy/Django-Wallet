# Generated by Django 4.0.6 on 2022-08-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywallet', '0005_alter_wallet_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pin',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='pin',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
