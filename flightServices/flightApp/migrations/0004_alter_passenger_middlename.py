# Generated by Django 3.2.6 on 2021-08-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0003_auto_20210819_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='middleName',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
