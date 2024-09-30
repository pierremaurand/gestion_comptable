from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    
    ADMINISTRATOR = 'ADMINISTRATOR'
    USER = 'USER'

    ROLE_CHOICES = (
        (ADMINISTRATOR, 'Administrateur'),
        (USER, 'Utilisateur'),
    )
    
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self.role == self.ADMINISTRATOR:
    #         group = Group.objects.get(name='Administrateurs')
    #         group.user_set.add(self)
    #     elif self.role == self.USER:
    #         group = Group.objects.get(name='Utilisateurs')
    #         group.user_set.add(self)