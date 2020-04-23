from rest_framework import viewsets
from .serializers import *
from .models import *
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [TokenHasReadWriteScope]

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [TokenHasReadWriteScope]

    def get_queryset(self):
        queryset = Test.objects.all()

        # Parse query that starts with "course_id"
        course = self.request.query_params.get('course_id', None)

        # Non-nil check
        if course is not None:
            # Filter among all tests against id
            queryset = queryset.filter(course__id=course)
        return queryset

class ListeningQuestionViewSet(viewsets.ModelViewSet):

    queryset = ListeningQuestion.objects.all()
    serializer_class = ListeningQuestionSerializer
    permission_classes = [TokenHasReadWriteScope]

    def get_queryset(self):
        queryset = ListeningQuestion.objects.all()

        # Parse query that starts with "test_id"
        test = self.request.query_params.get('test_id', None)

        # Non-nil check
        if test is not None:
            # Filter among all tests against id
            queryset = queryset.filter(test__id=test)
        return queryset

class ReadingQuestionViewSet(viewsets.ModelViewSet):

    queryset = ReadingQuestion.objects.all()
    serializer_class = ReadingQuestionSerializer
    permission_classes = [TokenHasReadWriteScope]

    def get_queryset(self):
        queryset = ReadingQuestion.objects.all()

        # Parse query that starts with "test_id"
        test = self.request.query_params.get('test_id', None)

        # Non-nil check
        if test is not None:
            # Filter among all tests against id
            queryset = queryset.filter(test__id=test)
        return queryset


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [TokenHasReadWriteScope]

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [TokenHasReadWriteScope]

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [TokenHasReadWriteScope]

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [TokenHasReadWriteScope]