# Generated by Django 4.1.7 on 2023-02-26 14:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgroupchats', '0003_alter_room_author_userroom_room_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(blank=True, through='webgroupchats.UserRoom', to=settings.AUTH_USER_MODEL),
        ),
    ]
