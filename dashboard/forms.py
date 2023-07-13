from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Staff, Contacts, TableBooking, CustomerReview, Gallery, Events, Company, AboutUs, SocialMediaLink
from menu.models import Order
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : '',
        'class': 'form-control rounded-xl'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : '',
        'class': 'form-control rounded-xl'
    }))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : '',
        'class': 'form-control rounded-xl'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : '',
        'class': 'form-control rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : '',
        'class': 'form-control rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : '',
        'class': 'form-control rounded-xl'
    }))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'email', 'subject', 'message', 'replied')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your Name',
        'class': 'form-control rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Your Email',
        'class': 'form-control rounded-xl'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Subject',
        'class': 'form-control rounded-xl'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder' : 'Message',
        'class': 'form-control rounded-xl'
    }))
    replied = forms.BooleanField(widget=forms.CheckboxInput(attrs={}))


class BookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ('name', 'email', 'phone_number', 'date', 'time', 'people', 'message', 'attended')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control rounded-xl'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded-xl'
    }))
    date = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded-xl'
    }))
    time = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded-xl'
    }))
    people = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded-xl'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control rounded-xl'
    }))
    attended = forms.BooleanField(widget=forms.CheckboxInput(attrs={}))

class AddStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

        widgets ={
            'user': forms.Select(attrs={
                'class': 'form-control'
            }),
            'passport_photo': forms.FileInput(attrs={
                'class': 'form-control'
            }), 
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }), 
            'company': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'about_description': forms.Textarea(attrs={
                'class': 'form-control'
            }), 
            'country': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'facebook': forms.URLInput(attrs={
                'class': 'form-control'
            }), 
            'twitter': forms.URLInput(attrs={
                'class': 'form-control'
            }), 
            'instagram': forms.URLInput(attrs={
                'class': 'form-control'
            }), 
            'linkedin': forms.URLInput(attrs={
                'class': 'form-control'
            }),
            'featured': forms.CheckboxInput(attrs={
                
            }),
            'admin': forms.CheckboxInput(attrs={
                
            }),
            
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ('name', 'photo', 'job_position', 'review_message', 'featured')

        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'job_position': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'review_message': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            
        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image','event', 'short_description', 'facebook', 'twitter', 'instagram', 'linkedin', 'featured')

        widgets ={
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'event': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'facebook': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'twitter': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'linkedin': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'featured': forms.CheckboxInput(attrs={
            }),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'image', 'price', 'short_description', 'features1', 'features2', 'features3', 'event_story')

        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'features1': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'features2': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'features3': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'event_story': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'logo', 'tagline', 'call1', 'call2', 'email1', 'email2', 'opening_time', 'closing_time', 'first_day', 'last_day', 'country', 'county', 'location', 'address')

        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'form-control'
            }), 
            'tagline': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'call1': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'call2': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email1': forms.EmailInput(attrs={
                'class': 'form-control'
            }), 
            'email2': forms.EmailInput(attrs={
                'class': 'form-control'
            }), 
            'opening_time': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'closing_time': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'first_day': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'last_day': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'country': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'county': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'location': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            
        }

class LinkForm(forms.ModelForm):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'

        widgets ={
                'name': forms.TextInput(attrs={
                    'class': 'form-control'
                }),
                'link': forms.URLInput(attrs={
                    'class': 'form-control'
                }),
                }
        
class AboutForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ('image', 'short_description', 'vision', 'mission', 'values', 'closing_description')

        widgets ={
            'image': forms.FileInput(attrs={
                    'class': 'form-control'
                }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'vision': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'mission': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'values': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'closing_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            
            }
class RecentSalesForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('transaction_id', 'served')
   
    served = forms.BooleanField(widget=forms.CheckboxInput(attrs={}))