# Generated by Django 3.0.3 on 2020-03-09 06:43

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20200304_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('theme', models.CharField(max_length=120)),
                ('value', models.CharField(max_length=120)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='exam.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('points', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None)),
                ('answer_image_path', models.CharField(max_length=120)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letters', to='exam.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('image_path', models.CharField(max_length=120)),
                ('answer_texts', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forms', to='exam.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image_path', models.CharField(max_length=120)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='exam.Course')),
            ],
        ),
    ]
