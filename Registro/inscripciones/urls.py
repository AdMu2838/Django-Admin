from django.urls import path

from .views import OrganizationListView,OrganizationDetailView,OrganizationCreateView

urlpatterns = [
    # URL para listar los clientes
    path('organizations/', OrganizationListView.as_view(), name='organization_list'),
    path('organization/<uuid:organization_id>/', OrganizationDetailView.as_view(), name='organization'),
    path('organizations/create/', OrganizationCreateView.as_view(), name='organization_create'),
]