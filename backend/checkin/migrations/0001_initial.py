# Generated by Django 3.1.7 on 2021-02-24 02:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_datetime', models.DateTimeField(verbose_name='From')),
                ('to_datetime', models.DateTimeField(verbose_name='To')),
                ('absence_type', models.CharField(choices=[('mission', 'Mission'), ('absence', 'Absence'), ('leave', 'Leave')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_datetime', models.DateTimeField(default=datetime.datetime(2021, 2, 23, 19, 35, 0, 870607), verbose_name='Log Time')),
                ('direction', models.CharField(choices=[('enter', 'Enter'), ('exit', 'Exit')], max_length=10)),
            ],
            options={
                'ordering': ['-log_datetime'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('personnel_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Contact Phone Number', max_length=128, region=None, verbose_name='Phone')),
                ('contract_expire_date', models.DateField(verbose_name='Contract Expire Date')),
                ('contract_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10, verbose_name='Contract Status')),
                ('account_no', models.PositiveIntegerField(verbose_name='Account No')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('entrance_time', models.TimeField(verbose_name='Enter')),
                ('entrance_low_range', models.TimeField(verbose_name='Enter Low Range')),
                ('entrance_high_range', models.TimeField(verbose_name='Enter High Range')),
                ('exit_time', models.TimeField(verbose_name='Exit')),
                ('exit_low_range', models.TimeField(verbose_name='Exit Low Range')),
                ('exit_high_range', models.TimeField(verbose_name='Exit High Range')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('driver_name', models.CharField(max_length=30, verbose_name='Driver Name')),
                ('driver_phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Driver Phone Number', max_length=128, region=None, verbose_name='Phone')),
                ('plate_no', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Plate No.')),
                ('rfid_no', models.CharField(max_length=100, unique=True, verbose_name='RFID No.')),
                ('transition_path', models.CharField(max_length=200, verbose_name='Path')),
                ('driver_license_exp', models.DateField(verbose_name='License Exp.')),
                ('insurance_exp', models.DateField(verbose_name='Insurance Exp.')),
                ('intelligent_card_exp', models.DateField(verbose_name='Intelligent Card Exp.')),
                ('health_card_exp', models.DateField(verbose_name='Health Card Exp.')),
                ('inspection_exp', models.DateField(verbose_name='Inspection Exp.')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkin.person')),
                ('shifts', models.ManyToManyField(to='checkin.Shift')),
                ('v_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkin.vehicletype', verbose_name='Class')),
            ],
        ),
        migrations.AddConstraint(
            model_name='shift',
            constraint=models.CheckConstraint(check=models.Q(('entrance_high_range__gt', django.db.models.expressions.F('entrance_time')), ('entrance_time__gt', django.db.models.expressions.F('entrance_low_range')), ('entrance_time__lt', django.db.models.expressions.F('exit_time')), ('exit_high_range__gt', django.db.models.expressions.F('exit_time')), ('exit_time__gt', django.db.models.expressions.F('exit_low_range'))), name='check_enter_and_exit_times'),
        ),
        migrations.AlterUniqueTogether(
            name='shift',
            unique_together={('entrance_time', 'exit_time')},
        ),
        migrations.AddField(
            model_name='log',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkin.vehicle'),
        ),
        migrations.AddField(
            model_name='absence',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkin.vehicle'),
        ),
        migrations.AddConstraint(
            model_name='absence',
            constraint=models.CheckConstraint(check=models.Q(to_datetime__gt=django.db.models.expressions.F('from_datetime')), name='to_datetime_gt_than_from_datetime'),
        ),
    ]
