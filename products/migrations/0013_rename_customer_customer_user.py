# Generated by Django 4.0.4 on 2022-04-20 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_customer_user_customer_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer',
            new_name='user',
        ),
    ]