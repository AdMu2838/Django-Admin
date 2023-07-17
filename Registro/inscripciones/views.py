from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView
from .forms import OrganizationForm
from .models.Organization import Organization

class OrganizationListView(ListView):
    model = Organization
    template_name = 'organization_list.html'
    context_object_name = 'organizations'

class OrganizationDetailView(View):
    def get(self, request, organization_id):
        organization = get_object_or_404(Organization, organization_id=organization_id)
        return render(request, 'organization_detail.html', {'organization': organization})

class OrganizationCreateView(View):
    def get(self, request):
        form = OrganizationForm()
        return render(request, 'organization_create.html', {'form': form})

    def post(self, request):
        form = OrganizationForm(request.POST)
        if form.is_valid():
            organization = form.save()
            return redirect('organization_list')  # Redirigir a la vista de lista
        return render(request, 'organization_create.html', {'form': form})