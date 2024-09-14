from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from apps.core.models.abstract import CreatedUpdatedAbstractModel


class Organization(MPTTModel, CreatedUpdatedAbstractModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Employee(CreatedUpdatedAbstractModel):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    hire_date = models.DateField()
    salary = models.PositiveIntegerField()
    organization = models.ForeignKey(
        "tree.Organization", on_delete=models.CASCADE, related_name="employees"
    )

    def __str__(self):
        return f"{self.full_name}"
