import json
import os

from django.core.management.base import BaseCommand, no_translations

from apps.product.models import Product


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Command(BaseCommand):
    help = "Populating initial database with the provided sample data"

    @no_translations
    def handle(self, *args, **kwargs):
        """
        handler for populating initial database with the provided sample data or if data exists, it bypasses.
        """
        data = Product.objects.all()

        if len(data) > 1:
            self.stdout.write("Data already exists")
        else:
            instances_to_create = []
            with open(os.path.join('apps', 'product', 'management', 'commands', 'populate_initial_db.py'), 'r') as file:
                for line in file:
                    data = json.loads(line)
                    if data:
                        instance = Product(
                            tags_from_description=tags_from_description)
                        instances_to_create.append(instance)

