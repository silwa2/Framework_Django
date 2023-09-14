from django.core.management import BaseCommand
from Framework_Django.Framework_Django.Project_HW.task_django.magaz.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John',
                    email='john@example.com',
                    phone='89034565432',
                    address='Russia',
                    registered_at='01.01.1888')
        user.save()
        self.stdout.write(f'{user}')
