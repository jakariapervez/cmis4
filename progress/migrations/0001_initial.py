# Generated by Django 2.1.7 on 2019-02-19 12:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_short_name', models.CharField(default='xxx', max_length=200)),
                ('package_detail_name', models.CharField(default='xxx', max_length=1000)),
                ('contractor_short_name', models.CharField(default='xxx', max_length=200)),
                ('start_date', models.DateField(default=datetime.datetime.now)),
                ('finish_date', models.DateField(default=datetime.datetime.now)),
                ('extended_date', models.DateField(blank=True, null=True)),
                ('contract_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
                ('billed_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
                ('estimated_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
                ('physical_progress', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('financial_progress', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContractComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('tradelicense', models.CharField(max_length=10)),
                ('Vat_registration', models.CharField(max_length=11)),
                ('TIN_No', models.CharField(max_length=12)),
                ('egp_id', models.CharField(max_length=14)),
                ('national_id', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division_name', models.CharField(max_length=100)),
                ('div_address', models.CharField(blank=True, max_length=250, null=True)),
                ('div_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.District')),
            ],
        ),
        migrations.CreateModel(
            name='Haor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('area', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('project_type', models.CharField(choices=[('Old', 'Rehablitation'), ('New', 'New Haor')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('start_point', models.DecimalField(blank=True, decimal_places=3, max_digits=13, null=True)),
                ('finish_point', models.DecimalField(blank=True, decimal_places=3, max_digits=13, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=3, max_digits=13, null=True)),
                ('volume', models.DecimalField(blank=True, decimal_places=3, max_digits=13, null=True)),
                ('vent_no', models.IntegerField(blank=True, null=True)),
                ('consultant_eng_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultant_engg', to=settings.AUTH_USER_MODEL)),
                ('contract_component_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.ContractComponent')),
                ('contract_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.Contract')),
                ('field_eng_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='field_engg', to=settings.AUTH_USER_MODEL)),
                ('haor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.Haor')),
                ('site_eng_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_engg', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progress_Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('quantity', models.DecimalField(blank=True, decimal_places=3, max_digits=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgressItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='EW', max_length=200)),
                ('unit', models.TextField(max_length=10)),
                ('quantity', models.DecimalField(blank=True, decimal_places=3, max_digits=13, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=3, max_digits=13, null=True)),
                ('startdate', models.DateField(default=datetime.datetime.now)),
                ('finshdate', models.DateField(default=datetime.datetime.now)),
                ('intervention_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.Intervention')),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wtype', models.CharField(choices=[('EMB', 'Embankment'), ('SUBEMB', 'Submersible,Embankment'), ('EXKHL', 'Khal Rexcavation'), ('EXRIV', 'River Reexcavation'), ('REG', 'Regulator'), ('CASW', 'Cause Way'), ('IRIN', 'Irigation Inlet'), ('WMGO', 'WMG Office')], max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='progress_quantity',
            name='progress_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.ProgressItem'),
        ),
        migrations.AddField(
            model_name='intervention',
            name='worktype_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.WorkType'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contractor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.Contractor'),
        ),
        migrations.AddField(
            model_name='contract',
            name='division_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress.Division'),
        ),
        migrations.AddField(
            model_name='contract',
            name='partner_contractor1_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partner_contractor1_id', to='progress.Contractor'),
        ),
        migrations.AddField(
            model_name='contract',
            name='partner_contractor2_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partner_contractor2_id', to='progress.Contractor'),
        ),
        migrations.AddField(
            model_name='contract',
            name='sde_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sde_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contract',
            name='so_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='so_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contract',
            name='xen_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='xen_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
