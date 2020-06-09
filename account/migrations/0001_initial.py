# Generated by Django 3.0.6 on 2020-06-07 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(default='default/profile.png', upload_to='Profiles')),
                ('bio', models.CharField(blank=True, max_length=100)),
                ('connection', models.CharField(blank=True, max_length=255)),
                ('follower', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]