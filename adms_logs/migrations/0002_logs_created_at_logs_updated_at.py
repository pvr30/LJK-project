# Generated by Django 4.1.3 on 2023-05-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adms_logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logs',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
