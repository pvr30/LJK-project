# Generated by Django 4.1.7 on 2023-05-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_assign_duration', '0010_remove_userroomassign_user_userroomassign_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroomassign',
            name='remain_duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
