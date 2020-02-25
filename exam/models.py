from django.db import models
import uuid

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=120)
    aliasName = models.CharField(max_length=120)
    description = models.CharField(max_length=200)


class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question_text = models.CharField(max_length=120)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    #TODO: add model Choice??
