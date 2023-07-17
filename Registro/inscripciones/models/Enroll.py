from django.db import models
import uuid

from .Student import Student
from .Group import Group
from .Organization import Organization

class Enroll(models.Model):
    enroll_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enroll_status = models.BooleanField(default=True)
    enroll_created = models.DateTimeField(auto_now_add=True)
    enroll_modified = models.DateTimeField(auto_now=True)

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_id.group_name + " " + self.student_id.user_id.user_name + " " + self.student_id.user_id.user_last_name + " " + self.organization_id.organization_name