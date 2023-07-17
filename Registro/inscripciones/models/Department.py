from django.db import models
import uuid

from .Organization import Organization

class Department(models.Model):
    department_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_name = models.CharField(max_length=100)
    department_status = models.BooleanField(default=True)
    department_created = models.DateTimeField(auto_now_add=True)
    department_modified = models.DateTimeField(auto_now=True)

    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name + " " + self.organization_id.organization_name