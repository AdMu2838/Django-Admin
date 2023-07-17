from django.db import models
import uuid

from .Organization import Organization

class Course(models.Model):
    course_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=100)
    course_status = models.BooleanField(default=True)
    course_created = models.DateTimeField(auto_now_add=True)
    course_modified = models.DateTimeField(auto_now=True)

    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # ideal plan
    # semester_id = models.ForeignKey('Semester', on_delete=models.CASCADE)
    # plan_id = models.ForeignKey('Plan', on_delete=models.CASCADE)
    # school_id = models.ForeignKey('School', on_delete=models.CASCADE)
    # department_id = models.ForeignKey('Department', on_delete=models.CASCADE)
    # faculty_id = models.ForeignKey('Faculty', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name + " " + self.organization_id.organization_name