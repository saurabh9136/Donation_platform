from django.utils import timezone
import uuid
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class NGOManager(BaseUserManager):
    def create_ngo(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        ngo = self.model(email=email, **extra_fields)
        ngo.password = make_password(password)  # Hash the password
        ngo.save(using=self._db)
        return ngo
    
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country_region = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    # Admin fields
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True
    )

class NGO(AbstractBaseUser):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    ngo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    ngo_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    contact_person = models.CharField(max_length=255)
    details = models.TextField(default="No details provided")
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)
    website_link = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country_region = models.CharField(max_length=100, null=True, blank=True)
    terms_conditions_path = models.FileField(upload_to='ngo_documents/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Inactive')
    ngo_picture = models.ImageField(upload_to='ngo_pictures/', null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.ngo_name

class Donation(models.Model):
    STATUS_CHOICES = [
        ('Initialized', 'Initialized'),
        ('Completed', 'Completed'),
    ]
    donation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id')   
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, to_field='ngo_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    platform_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Initialized')
    donation_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    tax_certificate_path = models.FileField(upload_to='donation_documents/', null=True, blank=True)
