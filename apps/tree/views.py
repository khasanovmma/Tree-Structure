from django.db.models import QuerySet
from django.http import JsonResponse
from django.views import generic

from apps.tree.api.serializers import OrganizationHierarchySerializer
from apps.tree.models import Organization


class OrganizationView(generic.ListView):
    template_name = "tree/tree_structure.html"
    context_object_name = "organizations"
    model = Organization

    def get_queryset(self) -> QuerySet[Organization]:
        return self.model.objects.filter(parent=None)[1:]


def organization_detail(request, pk):
    organization = Organization.objects.get(pk=pk)
    return JsonResponse(OrganizationHierarchySerializer(organization).data)
