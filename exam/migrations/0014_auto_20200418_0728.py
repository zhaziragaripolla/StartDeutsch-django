# Generated by Django 3.0.3 on 2020-04-18 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_auto_20200418_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingquestion',
            name='image_path',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
