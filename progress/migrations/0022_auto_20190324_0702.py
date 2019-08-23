# Generated by Django 2.0.3 on 2019-03-24 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0021_auto_20190322_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract_intervention',
            name='financial_weight',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.1, max_digits=4),
        ),
        migrations.AddField(
            model_name='contract_intervention',
            name='physical_weight',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='dpp_intervention',
            name='work_status',
            field=models.CharField(blank=True, choices=[('OG', 'OG'), ('COMP', 'COMP'), ('TO_BE_STARTED', 'TO_BE_STARTED')], default='OG', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='progressitem',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
    ]
