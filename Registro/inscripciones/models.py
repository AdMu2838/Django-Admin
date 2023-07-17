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
class Department(models.Model):
    department_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_name = models.CharField(max_length=100)
    department_status = models.BooleanField(default=True)
    department_created = models.DateTimeField(auto_now_add=True)
    department_modified = models.DateTimeField(auto_now=True)

    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name + " " + self.organization_id.organization_name
class Academic(models.Model):
    academic_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_name = models.CharField(max_length=100)
    academic_status = models.BooleanField(default=True)
    academic_created = models.DateTimeField(auto_now_add=True)
    academic_modified = models.DateTimeField(auto_now=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.academic_name + " " + self.department_id.department_name + " " + self.organization_id.organization_name