from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=120, unique=True)
    alias_name = models.CharField(max_length=120)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tests')

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    order_number = models.IntegerField()

    # Abstract Inheritance
    class Meta:
        abstract = True

class ListeningQuestion(Question):
    question_text = models.TextField(unique=True)
    audio_path = models.CharField(max_length=120)
    answer_choices = ArrayField(models.CharField(max_length=150), null=True, blank=True, default=list)
    correct_choice_index = models.IntegerField(default=0)

    class Meta:
        unique_together = ('question_text', 'audio_path', 'answer_choices')

    def __str__(self):
        return self.question_text

class ReadingQuestion(Question):
    section = models.IntegerField()
    image_path = models.CharField(max_length=120, blank=True) # Optional (don't put null=True)
    question_text = models.TextField(blank=True) # Optional (don't put null=True)
    question_texts = ArrayField(models.CharField(max_length=220), null=True, default=list)
    answer_image_paths = ArrayField(models.CharField(max_length=220), blank=True, null=True, default=list)
    correct_answers = ArrayField(models.BooleanField(), null=True, default=list)
    correct_choice_index = models.IntegerField(blank=True, null=True, default=None)
    description = models.CharField(max_length=180, blank=True)

    class Meta:
        unique_together = ('question_text', 'question_texts',)

    def __str__(self):
        return self.question_text

class Letter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='letters')
    title = models.CharField(max_length=120)
    # TODO: change to not-nil
    points = ArrayField(models.CharField(max_length=150), null=True)
    answer_image_path = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='forms')
    title = models.CharField(max_length=120)
    text = models.TextField(unique=True)
    image_path = models.CharField(max_length=120)
    answer_texts = ArrayField(models.CharField(max_length=150), null=True)

    def __str__(self):
        return self.title

class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='words')
    theme = models.CharField(max_length=120)
    value = models.CharField(max_length=120)

    class Meta:
        unique_together = ('theme', 'value',)

    def __str__(self):
        return '%s %s' % (self.theme, self.value)

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cards')
    image_url = models.CharField(max_length=120, unique=True)

