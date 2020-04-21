"""
This script is to load data from .csv files.
"""
from django.core.management import BaseCommand, CommandError
import csv
import os, re
from django.apps import apps
from exam.models import Course, Test, ListeningQuestion, ReadingQuestion, Card, Word
from django.db import transaction

class Command(BaseCommand):
    help = "Loads data from .csv file. CSV file name(s) should be passed." \
            "CSV files could contain different data referring to corresponding models.: "\
            "CSV files name specifies which data models is saved in it:" \
            "File name for test data: test[0-9].csv", \
            "card data model: card[0-9].csv, word data model: word[0-9].csv." \
            "Make sure load_initial_course_data was run before this command."

    def add_arguments(self, parser):
        parser.add_argument('filenames', nargs='+', type=str, help='Inserts data models from .csv files')

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write('Starting command execution')
            try:
                Course.objects.get(title="Listening")
                Course.objects.get(title="Reading")
                Course.objects.get(title="Speaking")
                Course.objects.get(title="Writing")
            except Course.DoesNotExist as e:
                raise CommandError("Course not found. "
                                   "Check if you run load_initial_course_data.py'".format(Course, str(e)))
            for filename in options['filenames']:
                self.stdout.write(self.style.SUCCESS('Reading:{}'.format(filename)))
                file_path = self.get_csv_file(filename)
                if re.search('listening', file_path):
                    self.stdout.write(self.style.SUCCESS('Parsing file with model "ListeningQuestion"'))
                    self.parse_listening_question_data(file_path)
                elif re.search('reading', file_path):
                    self.stdout.write(self.style.SUCCESS('Parsing file with model "ReadingQuestion"'))
                    self.parse_reading_question_data(file_path)
                elif re.search('card', file_path):
                    self.stdout.write(self.style.SUCCESS('Parsing file with model "Card"'))
                    self.parse_card_data(file_path)
                elif re.search('word', file_path):
                    self.stdout.write(self.style.SUCCESS('Parsing file with model "Word"'))
                    self.parse_word_data(file_path)
            self.stdout.write(self.style.SUCCESS('Transaction successfully commited.'))

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(app_path, "management",
                                 "commands", filename)
        return file_path

    def get_current_app_path(self):
        return apps.get_app_config('exam').path

    def parse_card_data(self, file_path):
        try:
            with open(file_path) as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    image_path = row['image_url']
                    try:
                        speaking_course = Course.objects.get(title="Speaking")
                        Card.objects.create(image_path=image_path, course=speaking_course)
                    except Exception as e:
                        raise CommandError("Error in inserting {}: {}".format(Card, str(e)))
        except FileNotFoundError:
            raise CommandError("File {} does not exist".format(file_path))

    def parse_word_data(self, file_path):
        try:
            with open(file_path) as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    theme = row['theme']
                    value = row['value']
                    try:
                        speaking_course = Course.objects.get(title="Speaking")
                        Word.objects.create(theme=theme, value=value, course=speaking_course)
                    except Exception as e:
                        raise CommandError("Error in inserting {}: {}".format(Card, str(e)))
        except FileNotFoundError:
            raise CommandError("File {} does not exist".format(file_path))

    def parse_listening_question_data(self, file_path):
        try:
            with open(file_path) as csv_file:
                reader = csv.DictReader(csv_file)
                listening_course = Course.objects.get(title="Listening")
                listening_test = Test.objects.create(course=listening_course)
                for row in reader:
                    # Parsing Listening question
                    question = ListeningQuestion()
                    question.test = listening_test
                    order_number = int(row['order_number'])
                    question.order_number = order_number
                    question.question_text = row['question_text']
                    question.audio_path = row['audio_path']
                    if 6 < order_number < 11:
                        raw_answer_choices = row['answer_choices']
                        answer_choices = [choice for choice in raw_answer_choices.split(';') if choice]
                        for choice in answer_choices:
                            question.answer_choices.append(choice)
                    question.correct_choice_index = row['correct_choice_index']
                    question.save()
        except FileNotFoundError:
            raise CommandError("File {} does not exist".format(file_path))

    def parse_reading_question_data(self, file_path):
        try:
            with open(file_path) as csv_file:
                reader = csv.DictReader(csv_file)
                reading_course = Course.objects.get(title="Reading")
                reading_test = Test.objects.create(course=reading_course)
                for row in reader:
                    # Parsing Reading question
                    question = ReadingQuestion()
                    question.test = reading_test
                    question.order_number = row['order_number']
                    question.section = row['section']
                    if row['section'] == '1':
                        # Parsing question texts
                        question.image_path = row['image_path']
                        raw_question_texts = row['question_texts']
                        question_texts = [text for text in raw_question_texts.split(';') if text]
                        for text in question_texts:
                            question.question_texts.append(text)
                            # Parsing correct answers
                            raw_correct_answers = row['correct_answers']
                            correct_answers = [answer for answer in raw_correct_answers.split(';') if answer]
                        for answer in correct_answers:
                            if answer.lower() in ['true', '1']:
                                question.correct_answers.append(True)
                            else:
                                question.correct_answers.append(False)
                    elif row['section'] == '2':
                        question.question_text = row['question_text']
                        question.correct_choice_index = row['correct_choice_index']
                         # Parsing answer image paths
                        raw_image_paths = row['answer_image_paths']
                        image_paths = [path for path in raw_image_paths.split(',') if path]
                        for path in image_paths:
                            question.answer_image_paths.append(path)
                    elif row['section'] == '3':
                        question.question_text = row['question_text']
                        question.correct_choice_index = row['correct_choice_index']
                        question.image_path = row['image_path']
                        question.description = row['description']
                    question.save()
        except FileNotFoundError:
            raise CommandError("File {} does not exist".format(file_path))