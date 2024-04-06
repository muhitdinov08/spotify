# Generated by Django 5.0.3 on 2024-03-18 15:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0005_alter_artist_id"),
        ("user", "0004_alter_user_artist_following_alter_user_followings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="artist_following",
            field=models.ManyToManyField(related_name="users", to="music.artist"),
        ),
        migrations.AlterField(
            model_name="user",
            name="followings",
            field=models.ManyToManyField(
                related_name="followers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]