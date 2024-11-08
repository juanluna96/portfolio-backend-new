from django.core.management.base import BaseCommand
from apps.information.models import Biography

class Command(BaseCommand):
    help = 'Seeds the database with sample Biography data'

    def handle(self, *args, **kwargs):
        Biography.objects.create(
            description="This is a sample description.",
            stacks_description="Django, React, PostgreSQL.",
            about_me="I am a software developer with 5 years of experience.",
            phone_1="1234567890",
            phone_2="0987654321",
            email_1="example1@example.com",
            email_2="example2@example.com"
        )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with Biography data'))
