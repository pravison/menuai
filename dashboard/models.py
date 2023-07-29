from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    passport_photo = models.ImageField(upload_to='img', blank=True, null=True)
    name = models.CharField(max_length=150,)
    position = models.CharField(max_length=150, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    about_description= models.TextField(max_length=1000, null=True, blank=True)
    company = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    waiter = models.BooleanField(default=False, blank=True, null=True,)
    on_shift = models.BooleanField(default=False, blank=True, null=True,)
    featured = models.BooleanField(default=False, blank=True, null=True,)
    admin = models.BooleanField(blank=True, null=True, default=False)
    

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.passport_photo.url
        except:
            url = ''
        return url
    
class Contacts(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=1000,)
    send_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Contacts'
        ordering = ['-send_at']

    def __str__(self):
        return f'send by {self.name} at {self.send_at}'
    
class TableBooking(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=16)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    people = models.IntegerField()
    message = models.TextField(max_length=400)
    send_at = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)

    def __str__(self):

        return f'table boked by {self.name} attending status {self.attended}'
    

class CustomerReview(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='img', blank=True, null=True)
    job_position = models.CharField(max_length=150, blank=True, null=True)
    review_message = models.TextField(max_length=1000)
    featured = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url
    

class Gallery(models.Model):
    image = models.ImageField(upload_to='img')
    event = models.CharField(max_length=50, blank=True, null=True, help_text='event the image was taken or name of the image')
    short_description = models.TextField(max_length=250, blank=True, null=True, help_text='event the image was taken or name of the image')
    facebook = models.URLField(blank=True, null=True, help_text='facebook link to the image post if was shared')
    twitter = models.URLField(blank=True, null=True, help_text='twitter link to the image tweet if was shared')
    instagram = models.URLField(blank=True, null=True, help_text='instagram link to the image post if was shared')
    linkedin = models.URLField(blank=True, null=True, help_text='linkedin link to the image post if was shared')
    featured = models.BooleanField(default=False, blank=True, null=True,)

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return f' image {self.id}'


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Events(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='img')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    short_description = models.TextField(max_length=500, blank=True, null=True)
    features1 = models.CharField(max_length=250, blank=True, null=True) 
    features2 = models.CharField(max_length=250, blank=True, null=True) 
    features3 = models.CharField(max_length=250, blank=True, null=True) 
    event_story = models.TextField(max_length=750, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='img', blank=True, null=True)
    tagline = models.CharField(max_length=300, blank=True, null=True)
    call1 = models.CharField(max_length=16, blank=True, null=True)
    call2 = models.CharField(max_length=16, blank=True, null=True)
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    opening_time = models.CharField(max_length=40, blank=True, null=True)
    closing_time = models.CharField(max_length=40, blank=True, null=True)
    first_day =models.CharField(max_length=40, blank=True, null=True)
    last_day = models.CharField(max_length=40, blank=True, null=True)
    country =models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=40, blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    created_at =models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at =models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url
    
class AboutUs(models.Model):
    image = models.ImageField(upload_to='img', blank=True, null=True)
    short_description = models.TextField(max_length=300, blank=True, null=True)
    vision = models.CharField(max_length=150, blank=True, null=True)
    mission = models.CharField(max_length=150, blank=True, null=True)
    values = models.CharField(max_length=150, blank=True, null=True)
    closing_description=models.TextField(max_length=250, blank=True, null=True)
    created_at =models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at =models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return f'{self.id}'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class SocialMediaLink(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name




   


    


