# Generated by Django 4.1.7 on 2023-05-23 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_delete_userroomassign'),
        ('user_assign_duration', '0003_remove_useracassign_user_useracassign_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useracassign',
            name='ac',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.ac'),
        ),
        migrations.AlterField(
            model_name='useracassign',
            name='room',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.room'),
        ),
    ]
