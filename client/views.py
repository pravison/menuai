from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Client, Domain
from django.contrib.auth import login
from django_tenants.utils import schema_context

from .forms import TenantRegistrationForm

def homePage(request):
    context = {}
    return render(request, 'homepage.html', context)

def tenantRegistration(request):
    if request.method == 'POST':
        form = TenantRegistrationForm(request.POST)
        if form.is_valid():
            tenant_name = form.cleaned_data['tenant_name']
            superuser_username = form.cleaned_data['superuser_username']
            superuser_email = form.cleaned_data['superuser_email']
            superuser_password1 = form.cleaned_data['superuser_password1']
            superuser_password2 = form.cleaned_data['superuser_password2']
            phone_number = form.cleaned_data['phone_number']
            # will write th elogic to handle ontrial and paid until
            on_trial = True
            paid_until = '2024-7-5'

            if superuser_password1 !=superuser_password2:
                messages.error(request, "the two password doesn't match")
                return render(request, 'superuser_registration.html')
            else:
                #create tenant
                new_tenant = Client(schema_name=tenant_name, name=tenant_name, admin_name=superuser_username, email=superuser_email, phone_number=phone_number, on_trial=on_trial, paid_until=paid_until)
                new_tenant.save()

                domain = Domain()
                domain.domain =tenant_name + '.localhost'
                domain.tenant = new_tenant
                domain.is_primary= True
                domain.save()

                # create superuser for new tenant
                with schema_context(new_tenant.schema_name):
                    user = User.objects.create_superuser(
                        username=superuser_username,
                        password=superuser_password1,
                        email=superuser_email,
                    )

                return redirect('http://www.' + domain.domain + ':8000/admin')
    else:
        form = TenantRegistrationForm()
    return render(request, 'superuser_registration.html', {'form':form})




