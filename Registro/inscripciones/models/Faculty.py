from django.db import models
import uuid

from .Organization import Organization

class Faculty(models.Model):
    faculty_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    faculty_name = models.CharField(max_length=100)
    faculty_status = models.BooleanField(default=True)
    faculty_created = models.DateTimeField(auto_now_add=True)
    faculty_modified = models.DateTimeField(auto_now=True)

    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty_name + " " + self.organization_id.organization_name