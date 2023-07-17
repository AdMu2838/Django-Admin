from django.db import models
import uuid

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