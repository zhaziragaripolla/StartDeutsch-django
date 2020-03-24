from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=120)
    aliasName = models.CharField(max_length=120)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tests')

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    order_number = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    # Abstract Inheritance
    class Meta:
        abstract = True
class ListeningQuestion(Question):
    question_text = models.TextField()
    audio_path = models.CharField(max_length=120)
    answer_choices = ArrayField(models.CharField(max_length=150), null=True, blank=True, default=list)
    correct_choice_index = models.DecimalField(max_digits=1, decimal_places=0)

    def __str__(self):
        return self.question_text

class ReadingQuestion(Question):
    section = models.DecimalField(max_digits=1, decimal_places=0)
    image_path = models.CharField(max_length=120, blank=True) # Optional (don't put null=True)
    question_text = models.TextField(blank=True) # Optional (don't put null=True)
    question_texts = ArrayField(models.CharField(max_length=220), blank=True, null=True, default=list)
    answer_image_paths = ArrayField(models.CharField(max_length=220), blank=True, default=list)
    correct_answers = ArrayField(models.BooleanField(), blank=True, default=list)
    correct_choice_index = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    description = models.CharField(max_length=180, blank=True)
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
    text = models.TextField()
    image_path = models.CharField(max_length=120)
    answer_texts = ArrayField(models.CharField(max_length=150), null=True)

    def __str__(self):
        return self.title

class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='words')
    theme = models.CharField(max_length=120)
    value = models.CharField(max_length=120)

    def __str__(self):
        return self.value

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cards')
    image_path = models.CharField(max_length=120)