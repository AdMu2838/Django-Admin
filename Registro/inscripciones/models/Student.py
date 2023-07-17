from django.db import models
import uuid

from .User import User
from .School import School
from .Organization import Organization

class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_status = models.BooleanField(default=True)
    student_created = models.DateTimeField(auto_now_add=True)
    student_modified = models.DateTimeField(auto_now=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.user_name + " " + self.user_id.user_last_name + " " + self.school_id.school_name + " " + self.organization_id.organization_name