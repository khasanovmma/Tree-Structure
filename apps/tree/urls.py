from django.urls import path

from apps.tree.views import OrganizationView, organization_detail

urlpatterns = [
    path("", OrganizationView.as_view(), name="organization"),
    path("<int:pk>/", organization_detail, name="organization_detail"),
]
