from django.core.management.base import BaseCommand
from ._pollsdata import *

class Command(BaseCommand):
    help = 'Prepopulates categories with questions and choices to vote'
    def handle(self, *args, **options):
        create_category(categories)
        self.stdout.write(self.style.SUCCESS("Successfully created Categories"))
        create_would_questions(would_questions)
        create_serious_questions(serious_questions)
        create_polit_questions(political)
        create_movie_questions(movie)
        create_preference_questions(vs)
        create_fun_questions(fun)
        self.stdout.write(self.style.SUCCESS("Successfully populated categories with questions!"))