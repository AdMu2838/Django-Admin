from django.db import models
import uuid

from .Organization import Organization

class Plan(models.Model):
    plan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan_year = models.CharField(max_length=4) # check this
    plan_status = models.BooleanField(default=True)
    plan_created = models.DateTimeField(auto_now_add=True)
    plan_modified = models.DateTimeField(auto_now=True)

    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.plan_year + " " + self.organization_id.organization_name