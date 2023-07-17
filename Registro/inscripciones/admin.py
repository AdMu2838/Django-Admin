from django.contrib import admin
from .models.Plan import Plan
from .models.Student import Student
from .models.Organization import Organization
from .models.Academic import Academic
from .models.Department import Department
from .models.User import User
from .models.User_Type import User_Type
from .models.Teacher import Teacher
from .models.Assignment import Assignment
from .models.Course import Course
from .models.School import School
from .models.Enroll import Enroll
from .models.Faculty import Faculty
from .models.Group import Group
from .models.Semester import Semester
# Register your models here.
admin.site.register(Organization)
admin.site.register(Academic)
admin.site.register(Department)
admin.site.register(User)
admin.site.register(User_Type)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(School)
admin.site.register(Enroll)
admin.site.register(Group)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Plan)
admin.site.register(Semester)
