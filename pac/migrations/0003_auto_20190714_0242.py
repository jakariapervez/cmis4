# Generated by Django 2.0.3 on 2019-07-13 20:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0002_auto_20190713_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_no', models.CharField(blank=True, max_length=25, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('Bank_name', models.CharField(max_length=60)),
                ('Bank_brach', models.CharField(max_length=60)),
                ('Total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('cheque_image', models.ImageField(upload_to='invoice_docs/%Y/%m/%d/')),
                ('issuing_date', models.DateField(default=django.utils.timezone.now)),
                ('uploaded_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceSupporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='invoice_docs/%Y/%m/%d/')),
                ('issuing_date', models.DateField(default=django.utils.timezone.now)),
                ('uploaded_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='cheque_details',
            name='document_id',
        ),
        migrations.AlterField(
            model_name='expenditure_details',
            name='Cheque_details_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pac.Invoice_details'),
        ),
        migrations.DeleteModel(
            name='Cheque_details',
        ),
        migrations.DeleteModel(
            name='ChequeImage',
        ),
        migrations.AddField(
            model_name='invoice_details',
            name='document_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pac.InvoiceImage'),
        ),
    ]
