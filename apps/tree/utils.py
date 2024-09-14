from django_seed import Seed

from apps.tree.models import Employee, Organization


class CreateFakeOrganizationHierarchyService:
    def __init__(self, num_levels: int, organization_per_level: int, total_employees: int):
        self.num_levels = num_levels  # Количество уровней
        self.organizations_per_level = (
            organization_per_level  # Подразделений на каждом уровне
        )
        self.total_employees = total_employees
        self.fake = Seed.faker(locale="ru-RU", codename="ru-RU")
        self.organizations = []

    def create_organizations(self):
        level_organizations = [
            self.create_organization(self.fake.company())
            for _ in range(self.organizations_per_level)
        ]
        self.organizations.extend(level_organizations)

        for _ in range(2, self.num_levels + 1):
            parent_organizations = level_organizations
            level_organizations = []
            for parent in parent_organizations:
                for _ in range(self.organizations_per_level):
                    organization = self.create_organization(self.fake.company(), parent)
                    level_organizations.append(organization)
            self.organizations.extend(level_organizations)

        print(f"{len(self.organizations)} organizations created.")

    def create_organization(self, name, parent=None):
        return Organization.objects.create(name=name, parent=parent)

    def create_employees(self):
        for _ in range(self.total_employees):
            Employee.objects.create(
                full_name=self.fake.name(),
                position=self.fake.job(),
                hire_date=self.fake.date_between(start_date="-25y", end_date="today"),
                salary=self.fake.random.uniform(50000, 500000),
                organization=self.fake.random.choice(self.organizations),
            )

        print(f"{self.total_employees} employees created.")

    def generate(self):
        self.create_organizations()
        self.create_employees()
