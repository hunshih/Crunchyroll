from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import requests

class Command(BaseCommand):
    help = 'Fetches data from a URL'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='The Django model to save the data into')
        parser.add_argument('url', type=str, help='The URL to fetch data from')

    def handle(self, *args, **options):
        model_name = options['model']
        url = options['url']
        try:
            response = requests.get(url)
            data = response.json()
            self.stdout.write(str(data))
            model = apps.get_model('api', model_name)
            instance = model()
            for key, value in data.items():
                setattr(instance, key, value)
                
            instance.save()
        except requests.exceptions.RequestException as e:
            raise CommandError('Failed to fetch data from "%s"' % url) from e
