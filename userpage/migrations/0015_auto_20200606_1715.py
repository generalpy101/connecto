# Generated by Django 3.0.6 on 2020-06-06 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0014_auto_20200606_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='postLike', to='userpage.Post'),
        ),
    ]