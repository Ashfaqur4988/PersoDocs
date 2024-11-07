from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#word file upload model
class Doc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
