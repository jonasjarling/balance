from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User


class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='news/', height_field=None, width_field=None, max_length=100,blank=True, null=True)
    headline = models.CharField(max_length=50)
    text = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.headline

    def as_dict(self):
        return {
            str(self.id): {
                "date": self.date,
                "picture": self.picture.url,
                "headline": self.headline,
                "text": self.text,
            },
        }

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class MyUserManager(BaseUserManager):
    def create_user(self, email,  password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


'''    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
'''