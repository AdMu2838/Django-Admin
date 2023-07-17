from django.contrib import admin
from .models import Organization,Academic,Department,User,User_Type,Teacher,Assignment\
    ,Course
# Register your models here.
admin.site.register(Organization)
admin.site.register(Academic)
admin.site.register(Department)
admin.site.register(User)
admin.site.register(User_Type)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(Course)
