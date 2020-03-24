from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers
from _collections import OrderedDict
from operator import itemgetter

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
"""
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'aliasName', 'description', 'tests']


class TestSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = ['id', 'course']

class ListeningQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListeningQuestion
        fields = '__all__'

        # What self means??
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret

class ReadingQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingQuestion
        fields = '__all__'

        # What self means??
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret

class LetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'