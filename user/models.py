from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    fitness_goal = models.TextField(null=True, blank=True)
    dietary_preference = models.TextField(null=True, blank=True)
    subscription_status = models.CharField(
        max_length=20,
        choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')],
        default='INACTIVE'
    )
    renewal_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.subscription_status == 'ACTIVE' and not self.renewal_date:
            self.renewal_date = date.today() + timedelta(days=30)
        super().save(*args, **kwargs)