# Generated by Django 2.0.3 on 2019-03-16 18:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0016_auto_20190309_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='progress_quantity',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='progressitem',
            name='finishdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='progressitem',
            name='startdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
