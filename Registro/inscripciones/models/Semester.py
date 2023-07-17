from django.db import models
import uuid

from .Organization import Organization

class Semester(models.Model):
    semester_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    semester_name = models.CharField(max_length=100)
    semester_status = models.BooleanField(default=True)
    semester_created = models.DateTimeField(auto_now_add=True)
    semester_modified = models.DateTimeField(auto_now=True)

    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.semester_name + " " + self.organization_id.organization_name