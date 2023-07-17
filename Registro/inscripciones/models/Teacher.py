from django.db import models
import uuid

from .Organization import Organization
from .User import User

class Teacher(models.Model):
    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher_name = models.CharField(max_length=100)
    teahcer_email = models.EmailField(max_length=254) # check this
    teacher_status = models.BooleanField(default=True)
    teacher_created = models.DateTimeField(auto_now_add=True)
    teacher_modified = models.DateTimeField(auto_now=True)

    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name + " " + self.organization_id.organization_name