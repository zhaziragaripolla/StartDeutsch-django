# Generated by Django 3.0.3 on 2020-03-21 17:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20200321_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeningquestion',
            name='answer_choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), blank=True, default=list, null=True, size=None),
        ),
    ]
