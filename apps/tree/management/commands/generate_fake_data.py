from django.core.management.base import BaseCommand

from apps.tree.utils import CreateFakeOrganizationHierarchyService


class Command(BaseCommand):
    help = "This command to generate populate db with fake data"

    def add_arguments(self, parser):
        parser.add_argument("num_levels", type=int, default=5)
        parser.add_argument("organizations_per_level", type=int, default=5)
        parser.add_argument("total_employees", type=int, default=50000)

    def handle(self, *args, **options):
        params = {
            "num_levels": options["num_levels"],
            "organization_per_level": options["organizations_per_level"],
            "total_employees": options["total_employees"],
        }
        generator_fake_data = CreateFakeOrganizationHierarchyService(**params)
        generator_fake_data.generate()
