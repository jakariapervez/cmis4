# Generated by Django 2.2.3 on 2019-07-15 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0009_auto_20190715_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice_details',
            old_name='Bank_branch',
            new_name='BatchType',
        ),
        migrations.RenameField(
            model_name='invoice_details',
            old_name='Bank_name',
            new_name='Description',
        ),
    ]