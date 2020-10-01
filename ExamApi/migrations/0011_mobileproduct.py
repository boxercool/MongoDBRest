# Generated by Django 3.0.5 on 2020-10-01 05:44

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApi', '0010_auto_20200930_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileProduct',
            fields=[
                ('Productid', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('Productname', models.CharField(max_length=200)),
                ('Productdetails', jsonfield.fields.JSONField()),
            ],
        ),
    ]