from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
)

from apps.tree.models import Employee, Organization


class OrganizationSerializer(ModelSerializer):
    has_children = SerializerMethodField()

    def get_has_children(self, organization: Organization) -> bool:
        return organization.children.exists()

    class Meta:
        model = Organization
        fields = ["id", "name", "has_children", "parent"]


class EmployeeSerializer(ModelSerializer):
    organization = StringRelatedField()

    class Meta:
        model = Employee
        fields = ["full_name", "position", "hire_date", "salary", "organization"]


class OrganizationHierarchySerializer(ModelSerializer):
    children = OrganizationSerializer(many=True)
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = Organization
        fields = ["children", "employees"]
