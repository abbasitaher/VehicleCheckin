# Generated by Django 3.1.6 on 2021-02-20 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_api', '0005_auto_20210216_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='driver',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.DeleteModel(
            name='Mission',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
