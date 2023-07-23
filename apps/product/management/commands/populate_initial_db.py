import json
import os

from django.core.management.base import BaseCommand, no_translations

from apps.product.models import Product


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))


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
            with open(os.path.join(BASE_DIR, 'apps', 'product', 'dump_data', 'ss_input_data_sample.jsonl'), 'r') as file:
                for line in file:
                    data = json.loads(line)
                    if data:
                        instance = Product(
                            jan=data.get('jan'),
                            product_name=data.get('product_name'),
                            attributes=data.get('attributes'),
                            maker=data.get('maker'),
                            brand=data.get('brand'),
                            tags_from_description=data.get('tags_from_description'),
                            tags_from_review=data.get('tags_from_review'),
                        )
                        instances_to_create.append(instance)

            Product.objects.bulk_create(instances_to_create)
            self.stdout.write("Data upload successful")
