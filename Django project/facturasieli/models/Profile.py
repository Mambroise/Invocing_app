# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Profile.py
# Author : Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from facturasieli.models.Company import Company
from facturasieli.models.Role import Role
from facturasieli.models.utils import get_avatar_path


class ProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        
        # Créer l'utilisateur Django
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        
        # Créer le profil
        profile = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        profile.save(using=self._db)
        return profile

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, first_name, last_name, password, **extra_fields)

class Profile(AbstractBaseUser):
    last_request_timestamp = models.DateTimeField(_("Last Request Timestamp"), auto_now_add=True)
    enable_2fa = models.BooleanField(_("Enable 2FA"), default=False)
    avatar = models.ImageField(_("Avatar"), default='default_avatar.jpg', upload_to=get_avatar_path)
    email = models.EmailField(_("Email"), unique=True)
    first_name = models.CharField(_("First Name"), max_length=150)
    last_name = models.CharField(_("Last Name"), max_length=150)
    password = models.CharField(_("Password"), max_length=255)

    role = models.ManyToManyField(Role, related_name='users')
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='employees', null=True)
    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'
