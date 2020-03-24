from exam.models import Course
from django.core.management import BaseCommand

ALREADY_LOADED_ERROR_MESSAGE = """
Course data is already loaded.
"""

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Course.objects.exists():
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        listening_course = Course()
        listening_course.title = "Listening"
        listening_course.alias_name = "Hören"
        listening_course.description = ""
        listening_course.save()
