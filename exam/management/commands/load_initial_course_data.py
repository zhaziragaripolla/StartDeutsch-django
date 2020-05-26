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
            Course.objects.create(title="Hören",
                              alias_name="Listening",
                              description= "")

            Course.objects.create(title="Lesen",
                              alias_name="Reading",
                              description="")

            Course.objects.create(title="Bitten formulieren",
                              alias_name="Cards",
                              description="")

            Course.objects.create(title="Fragen formulieren",
                              alias_name="Words",
                              description="")
        except Exception as e:
            raise CommandError("Error in inserting {}: {}".format(
                self.Course, str(e)))
        self.stdout.write(self.style.SUCCESS('Course models loaded'))
