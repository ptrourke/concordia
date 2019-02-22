from django.core.management.base import BaseCommand
from concordia.models import Asset


class Command(BaseCommand):
    help = "Populate the year attribute for Assets"

    def handle(self, **options):
        assets = Asset.objects.all().prefetch_related("item")
        for asset in assets:
            metadata = asset.item.metadata
            date_keys = metadata["item"]["dates"][0].keys()
            asset.year = date_keys
            asset.save()
