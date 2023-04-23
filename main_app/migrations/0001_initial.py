# Generated by Django 4.1.7 on 2023-04-02 09:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AC',
            fields=[
                ('room_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('ac_esp', models.BooleanField(default=False)),
                ('lock', models.BooleanField(default=False)),
                ('ping', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.ac')),
            ],
        ),
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('ckt_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('panel_id', models.CharField(max_length=255)),
                ('esp_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.ac')),
            ],
        ),
    ]