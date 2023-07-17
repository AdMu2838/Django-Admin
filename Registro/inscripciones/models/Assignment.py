from django.db import models
import uuid

from .Academic import Academic
from .Teacher import Teacher
from .Course import Course
from .Organization import Organization

class Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    assignment_status = models.BooleanField(default=True)
    assignment_created = models.DateTimeField(auto_now_add=True)
    assignment_modified = models.DateTimeField(auto_now=True)

    academic_id = models.ForeignKey(Academic, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.academic_id) + " " + self.teacher_id.teacher_name + " " + self.course_id.course_name + " " + self.organization_id.organization_name
