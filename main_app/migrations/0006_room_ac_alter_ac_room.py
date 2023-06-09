# Generated by Django 4.1.7 on 2023-04-02 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_ac_ac_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='ac',
            field=models.ManyToManyField(blank=True, null=True, related_name='ac', to='main_app.ac'),
        ),
        migrations.AlterField(
            model_name='ac',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='main_app.room'),
        ),
    ]
