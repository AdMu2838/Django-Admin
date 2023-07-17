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


class User_Type(models.Model):
    user_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type_name = models.CharField(max_length=100)
    user_type_status = models.BooleanField(default=True)
    user_type_created = models.DateTimeField(auto_now_add=True)
    user_type_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_type_name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_type_name'], name='unique_user_type_name')
        ]