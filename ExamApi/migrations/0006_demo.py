# Generated by Django 3.0.5 on 2020-09-25 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApi', '0005_auto_20200924_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dname', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Duse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Demo_Use', to='ExamApi.Use')),
            ],
        ),
    ]
