from django.db import models
import uuid

from .Organization import Organization

class School(models.Model):
    school_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_name = models.CharField(max_length=100)
    school_status = models.BooleanField(default=True)
    school_created = models.DateTimeField(auto_now_add=True)
    school_modified = models.DateTimeField(auto_now=True)

    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name + " " + self.organization_id.organization_name