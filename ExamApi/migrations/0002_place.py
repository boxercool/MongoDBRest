# Generated by Django 3.0.5 on 2020-09-24 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placename', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('alname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_album', to='ExamApi.Album')),
            ],
        ),
    ]
