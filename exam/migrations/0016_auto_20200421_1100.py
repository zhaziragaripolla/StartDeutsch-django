# Generated by Django 3.0.3 on 2020-04-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0015_auto_20200418_0731'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='listeningquestion',
            unique_together={('question_text', 'audio_path', 'answer_choices')},
        ),
    ]
