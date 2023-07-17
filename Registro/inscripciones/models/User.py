from django.db import models
import uuid

from .User_Type import User_Type

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_dni = models.IntegerField(unique=True)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_dob = models.DateField()
    user_email = models.EmailField(max_length=254)
    # add user phone
    user_type_id = models.ForeignKey(User_Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_last_name + " " + self.user_name + "->" + self.user_type_id.user_type_name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_dni'], name='unique_user_dni'),
            models.UniqueConstraint(fields=['user_email'], name='unique_user_email')
        ]