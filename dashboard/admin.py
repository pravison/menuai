from django.contrib import admin
from .models import Staff, Contacts, TableBooking, Gallery, Events, CustomerReview, Company, AboutUs, SocialMediaLink

# Register your models here.
admin.site.register(Staff)
admin.site.register(Contacts)
admin.site.register(TableBooking)
admin.site.register(Gallery)
admin.site.register(Events)
admin.site.register(CustomerReview)
admin.site.register(Company)
admin.site.register(AboutUs)
admin.site.register(SocialMediaLink)
