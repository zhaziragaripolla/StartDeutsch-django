# Generated by Django 3.0.3 on 2020-03-27 10:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('aliasName', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
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
            name='Test',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='exam.Course')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingQuestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('order_number', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('section', models.DecimalField(decimal_places=0, max_digits=1)),
                ('image_path', models.CharField(blank=True, max_length=120)),
                ('question_text', models.TextField(blank=True)),
                ('question_texts', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=220), blank=True, default=list, null=True, size=None)),
                ('answer_image_paths', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=220), blank=True, default=list, size=None)),
                ('correct_answers', django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(), blank=True, default=list, size=None)),
                ('correct_choice_index', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('description', models.CharField(blank=True, max_length=180)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Test')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListeningQuestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('order_number', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('question_text', models.TextField()),
                ('audio_path', models.CharField(max_length=120)),
                ('answer_choices', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), blank=True, default=list, null=True, size=None)),
                ('correct_choice_index', models.DecimalField(decimal_places=0, max_digits=1)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Test')),
            ],
            options={
                'abstract': False,
            },
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
