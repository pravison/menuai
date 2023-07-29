from django.db.models.signals import post_save
from django.shortcuts import redirect
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction
from client.models import Client
from django_tenants.utils import schema_context

@receiver(post_save, sender=Client)
def create_tenant_superuser(sender, instance, created, **kwargs):
    if created:
        #create new user as the superuser
        with schema_context(instance.schema_name):
            user = User.objects.create_superuser(
                username=f"{instance.schema_name}",
                password="zxcvbnm09",
                email = instance.email,
            )
            user.tenant = instance
            user.save()
            transaction.on_commit(lambda: print('super user created for tenant {instance.schema_name}'))

            