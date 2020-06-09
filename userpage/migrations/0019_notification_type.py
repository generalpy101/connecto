# Generated by Django 3.0.6 on 2020-06-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0018_auto_20200609_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('Liked', 'liked'), ('Followed', 'followed')], default='liked', max_length=255),
        ),
    ]