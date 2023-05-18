from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    nick_name = models.CharField(_('nick name'), max_length=150, blank=True)

