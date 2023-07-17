from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import ListView

from .models.Organization import Organization

class OrganizationListView(ListView):
    model = Organization
    template_name = 'organization_list.html'
    context_object_name = 'organizations'

class OrganizationDetailView(View):
    def get(self, request, organization_id):
        organization = get_object_or_404(Organization, organization_id=organization_id)
        return render(request, 'organization_detail.html', {'organization': organization})