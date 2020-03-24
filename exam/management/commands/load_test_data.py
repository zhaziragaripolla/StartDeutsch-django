from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from exam.models import Course, Test, ListeningQuestion, ReadingQuestion
from pytz import UTC
from django.contrib.postgres.fields import ArrayField

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet model"

    def handle(self, *args, **options):
        listening_course = Course.objects.get(title="Listening")
        listening_test = Test()
        listening_test.course = listening_course
        listening_test.save()

        reading_course = Course.objects.get(title="Reading")
        reading_test = Test()
        reading_test.course = reading_course
        reading_test.save()

        for row in DictReader(open('./test1.csv')):
            print(row['question_type'])

            # Parsing Listening question
            if row['question_type']=='listening':
                question = ListeningQuestion()
                question.test = listening_test
                question.order_number = row['order_number']
                question.text = row['question_text']
                if row['is_multiple_choice']=='TRUE':
                    raw_answer_choices = row['answer_choices']
                    answer_choices = [choice for choice in raw_answer_choices.split(',') if choice]
                    for choice in answer_choices:
                        question.answer_choices.append(choice)
                question.correct_choice_index = row['correct_answers']
                print("New listening question is added")
                question.save()

            # Parsing Reading question
            elif row['question_type']=='reading':
                question = ReadingQuestion()
                question.test = reading_test
                question.order_number = row['order_number']
                question.section = row['section']
                if row['section'] == '1':
                    # Parsing question texts
                    raw_question_texts = row['question_text']
                    question_texts = [text for text in raw_question_texts.split(',') if text]
                    for text in question_texts:
                        question.question_texts.append(text)

                    # Parsing correct answers
                    raw_correct_answers = row['correct_answers']
                    correct_answers = [answer for answer in raw_correct_answers.split(',') if answer]
                    for answer in correct_answers:
                        if answer.lower() in ['true', '1']:
                            question.correct_answers.append(True)
                        else: question.correct_answers.append(False)
                elif row['section'] == '2':
                    question.question_text = row['question_text']
                    question.correct_choice_index = row['correct_answers']

                    # Parsing answer image paths
                    raw_image_paths = row['image_path']
                    image_paths = [path for path in raw_image_paths.split(',') if path]
                    for path in image_paths:
                        question.answer_image_paths.append(path)
                elif row['section'] == '3':
                    question.question_text = row['question_text']
                    question.correct_choice_index = row['correct_answers']
                    question.image_path = row['image_path']
                    question.description = row['reading_question_description']
                question.save()
