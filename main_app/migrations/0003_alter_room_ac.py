# Generated by Django 4.1.7 on 2023-04-02 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_room_uuid_ac_ac_uuid_ac_room_alter_room_ac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='ac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ac', to='main_app.ac'),
        ),
    ]
