from django.contrib.auth.models import User
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=200)
    admin_name =models.CharField(max_length=200, blank=True, null=True)
    paid_until = models.DateField(blank=True, null=True)
    on_trial = models.BooleanField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    #schema will be automatically created and synced when saved
    auto_create_schema= True
    auto_drop_schema = True


    def __str__(self):
        return str(self.name)

class Domain(DomainMixin):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_saas_admin = models.BooleanField(default=False)