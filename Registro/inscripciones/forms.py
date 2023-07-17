from .models.Organization import Organization
from django import forms
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ('organization_name',)