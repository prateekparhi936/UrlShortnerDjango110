from django.core.management.base import BaseCommand, CommandError
from shortener.models import MyUrlShortner

class Command(BaseCommand):
    help = 'Refreshes All Url Shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)        ## --items (optional)  , items(required)
        # parser.add_argument('item',type=int)

    def handle(self, *args, **options):
        return MyUrlShortner.objects.refresh_shortcode(items=options['items'])