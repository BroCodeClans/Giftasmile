from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from phone_field import PhoneField
from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):

    objects = UserManager()

    username = None
    first_name = None
    last_name = None

    email = models.EmailField(unique=True, blank=False,
    error_messages={'unique': "A user with that email already exists.", })
    role = models.CharField(max_length=25, error_messages={'required': "Role must be provided"}, 
    null=False, blank=False)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [role]

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    

class UserProfile(models.Model):

    Gender = (
        ('M','Male'),
        ('F','Female'),
        ('O', 'Other'),
        ('U', 'Undisclosed')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    gender = models.CharField(choices=Gender, max_length=10, blank=True, null=True, default="U")
    date_of_join = models.DateTimeField(default=datetime.now())
    contact_no = PhoneField()
    address = models.TextField(max_length=200, null=False, blank=False) 
    pincode = models.CharField(max_length=6, null=False, blank=False)
    occupation = models.CharField(max_length=50, null=False, blank=False)

    

class InstitutionProfile(models.Model):

    Type = (
        ('PR', 'Private Sector'),
        ('NG', 'NGO'),
        ('NP', 'NPO'),
        ('PU', 'Public Sector'),
        ('F', 'Foreign Institution'),
        ('I', 'Individual')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution_type = models.CharField(choices=Type, max_length=3, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    date_of_join = models.DateTimeField(default=datetime.now())
    unique_business_re_code = models.CharField(max_length=100, null=False, blank=False, unique=True)
    gst_number = models.CharField(max_length=100, null=False, blank=False, unique=True)
    address = models.TextField(max_length=200, null=False, blank=False) 
    liason_name = models.CharField(max_length=100, null=False, blank=False)
    liason_designation = models.CharField(max_length=100, null=False, blank=False)
    contact_no = PhoneField()


class VolunteerProfile(models.Model):
    Gender = (
        ('M','Male'),
        ('F','Female'),
        ('O', 'Other'),
        ('U', 'Undisclosed')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    gender = models.CharField(choices=Gender, max_length=10, blank=True, null=True, default="U")
    date_of_join = models.DateTimeField(default=datetime.now())
    address = models.TextField(max_length=200, null=False, blank=False) 
    pincode = models.CharField(max_length=6, null=False, blank=False)
    occupation = models.CharField(max_length=50, null=False, blank=False)


class Ranking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0, null=False, blank=False)
