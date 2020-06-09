# Generated by Django 3.0.6 on 2020-06-02 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0003_auto_20200602_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='connection',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]