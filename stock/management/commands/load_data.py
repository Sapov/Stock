from django.core.management import BaseCommand
from stock.models import Stock, Category, Equipment

class Command(BaseCommand):
    def handle(self, *args, **options):
        # for data in
        ...

