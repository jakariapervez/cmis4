# Generated by Django 2.0.3 on 2019-07-16 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0011_auto_20190715_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget_allocation',
            old_name='Dpp_allocation_id',
            new_name='Dpp_allocation',
        ),
    ]
