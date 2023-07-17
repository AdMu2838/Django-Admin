from django.db import models
import uuid

class Organization(models.Model):
    organization_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization_name = models.CharField(max_length=50)
    organization_status = models.BooleanField(default=True)
    organization_created = models.DateTimeField(auto_now_add=True)
    organization_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization_name
    
