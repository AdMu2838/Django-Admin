from django.db import models
import uuid

from .Assignment import Assignment
from .Teacher import Teacher
from .Organization import Organization

class Group(models.Model):
    group_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_name = models.CharField(max_length=100)
    group_status = models.BooleanField(default=True)
    group_created = models.DateTimeField(auto_now_add=True)
    group_modified = models.DateTimeField(auto_now=True)

    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name + " " + str(self.assignment_id) + " " + self.teacher_id.teacher_name + " " + self.organization_id.organization_name