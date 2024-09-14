from django.contrib.admin import ModelAdmin, register
from mptt.admin import MPTTModelAdmin

from apps.tree.models import Employee, Organization


@register(Organization)
class OrganizationAdmin(MPTTModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]
    raw_id_fields = ["parent"]


@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = [
        "id",
        "full_name",
        "position",
        "organization",
        "salary",
        "hire_date",
        "updated_at",
    ]
    list_display_links = ["id", "full_name", "position"]
    search_fields = ["full_name", "position", "organization__name"]
    raw_id_fields = ["organization"]
