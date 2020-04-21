from exam.models import Course
from django.core.management import BaseCommand, CommandError
ALREADY_LOADED_ERROR_MESSAGE = """
Course data is already loaded.
"""

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Course.objects.exists():
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        try:
            Course.objects.create(title="Listening",
                              alias_name="Hören",
                              description= "")

            Course.objects.create(title="Reading",
                              alias_name="Hören",
                              description="")

            Course.objects.create(title="Speaking",
                              alias_name="Sprechen",
                              description="")

            Course.objects.create(title="Writing",
                              alias_name="Schreiben",
                              description="")
        except Exception as e:
            raise CommandError("Error in inserting {}: {}".format(
                self.Course, str(e)))
        self.stdout.write(self.style.SUCCESS('Course models loaded'))
