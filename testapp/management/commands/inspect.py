from django.core.management.base import BaseCommand
from testapp.models.libraries import Library

TBL_NAMES = {
    'lib': {
        'table': Library,
        'aliasses': { 'bookcaches', 'libraries', 'library', 'bookcases', 'bookcase' }
    }
}

class Command(BaseCommand):
    help = "Inspect data tables"

    def handle(self, *args, **options):
        if len(args) <= 0:
            return
        match args[0].lower():
            case 'meta':
                spec = 'names'
                if len(args) >= 2:
                    spec = args[1]
                match spec.lower():
                    case 'names':
                        ...

