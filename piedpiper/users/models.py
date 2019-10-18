import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser,  BaseUserManager, UserManager
import django.core.validators
from django.contrib.auth.models import AbstractBaseUser
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.core import validators
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,username,email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        #if not self.username:
        #   self.username = self.id.hex

        user = self.model(is_active=False,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,username=None,email=None, password=None, **extra_fields):
        
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


@python_2_unicode_compatible
class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    username = models.CharField(_('username'), max_length=50, blank=True, null=True, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
    })
    first_name = models.CharField(blank=True, null=True,max_length=30)
    last_name  = models.CharField(blank=True, null=True,max_length=30)

    objects = CustomUserManager() 
    email = models.EmailField(max_length=70, unique=True)
    #email = models.EmailField(_('email address'), unique=True, null=True)
    #first_name = models.CharField(max_length=25)
    #last = models.CharField(max_length=25=True)
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username
    
    #def save(self, *args, **kwargs):
    #    if not self.username:
    #       self.username = self.id.hex
    #    return super(User, self).save(*args, **kwargs)
    #REQUIRED_FIELDS = ['email']
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['email']
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
