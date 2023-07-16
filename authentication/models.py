from django.contrib.auth.models import AbstractUser, Group as AuthGroup
from django.db import models

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    main_location = models.CharField(max_length=100, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    interests = models.CharField(max_length=255, blank=True, null=True)
    groups = models.ManyToManyField(AuthGroup, related_name='home_users')
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='home_users',
        help_text='Specific permissions for this user.',
        related_query_name='home_user',
    )
    def __str__(self):
        return self.username
    
class PhotoImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos')
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title