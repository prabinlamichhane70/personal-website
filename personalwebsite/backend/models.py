from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email,  name=None, password=None, password2=None,**extra_fields):
      
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
      )

      user.set_password(password)
      user.is_user = True
      user.save(using=self._db)
      return user

  def create_superuser(self, email,name=None, password=None,**extra_fields):
      user = self.create_user(
          email,
          password=password,
          name=name,
      )
      user.is_admin = True
      user.is_superuser =True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser,PermissionsMixin):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200,null=True, blank=True)
  is_admin = models.BooleanField(default=False)
  is_editor = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_active= models.BooleanField(default=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):
        return self.name or self.email

#   def has_perm(self, perm, obj=None):
#        return self.is_admin or self.is_vendor  # Include additional permissions as needed

#   def has_module_perms(self, app_label):
#       return True

  @property
  def is_staff(self):
      return self.is_admin +self.is_editor
  

class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True, related_name='editor')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=200)
    phone_number = models.IntegerField()



    def __str__(self):
        return self.user.name
