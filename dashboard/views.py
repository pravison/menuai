from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import SignUpForm, AddStaffForm, ContactForm, BookingForm, ReviewForm, GalleryForm, EventForm, LinkForm, CompanyForm, AboutForm, RecentSalesForm
from . models import Staff, Contacts, TableBooking, CustomerReview, Gallery, Events, Company, AboutUs, SocialMediaLink
from menu.models import Order, OrderItem, Customer, Menu
import datetime
from django.db.models import F, Sum, Avg
from django.utils import timezone
import copy

# Create your views here.
@login_required
def dashboard(request):
    year = datetime.date.today().year
    month = datetime.date.today().month
    today = timezone.now().date()
    menu = Menu.objects.all()
    customers = Customer.objects.all().filter(created_at__year=year)
    t = Order.objects.all().filter(date_orderd__date=today, complete=True)
    m = Order.objects.all().filter(date_orderd__month=month, complete=True)
    y = Order.objects.all().filter(date_orderd__year=year, complete=True)
    tsum= 0
    ttotal= 0
    tcustomer = t.count() #am assuming every customer nade one order which is a wrong assumption i will have to correct
    msum=0
    mtotal=0
    mcustomer = m.count()#am assuming every customer nade one order which is a wrong assumption i will have to correct
    ysum=0
    ytotal=0
    ycustomer= y.count()#am assuming every customer nade one order which is a wrong assumption i will have to correct
    arrays =[]
    unique=[]
    
    for x in t: 
        toi = x.orderitem_set.all()   
        tsum +=x.get_cart_total
        ttotal +=x.get_cart_items  
        '''for s in toi:
            s={'name':s.menu.name, 'quantity':s.quantity, 'total':s.get_total}
            arrays.append(s)  
                
     
        array_dict ={} 
        for array in arrays:
            array_name = array["name"]
            array_quantity = array["quantity"]
            array_total = array["total"]
            if array_name in array_dict:
                #product already exists
                array_dict[array_name] += array_quantity
                array_dict[array_name] += array_total
            else:
                #new product add to dictionart
                array_dict[array_name] = array_quantity
                array_dict[array_name] = array_total
            #print(f'array: {array_name}, quantity: {array_quantity}')'''

    for x in m:
        moi= x.orderitem_set.all()
        msum += x.get_cart_total
        mtotal +=x.get_cart_items
        '''for s in moi:
            s={'name':s.menu.name, 'quantity':s.quantity, 'total':s.get_total}
            arrays.append(s) 
            array_dict ={} 
            for array in arrays:
                array_name = array["name"]
                array_quantity = array["quantity"]
                array_total = array["total"]
                if array_name in array_dict:
                    #product already exists
                    array_dict[array_name] += array_quantity
                    array_dict[array_name] += array_total
                else:
                    #new product add to dictionart
                    array_dict[array_name] = array_quantity
                    array_dict[array_name] = array_total
                print(f'array: {array_name}, quantity: {array_quantity}')'''
 
    for x in y:
        yoi= x.orderitem_set.all()
        ysum +=x.get_cart_total
        ytotal +=x.get_cart_items
    
    
    context={
        't':t,
        'm':m,
        'y':y,
        'tsum': tsum,
        'ttotal':ttotal,
        'msum':msum,
        'mtotal': mtotal,
        'ysum': ysum,
        'ytotal':ytotal,
        'tcustomer':tcustomer,
        'mcustomer' :mcustomer,
        'ycustomer':ycustomer,
        'moi':moi,
        'yoi':yoi,
    }
    return render(request, 'dashboard.html', context)

@login_required
def sales(request):
    year = datetime.date.today().year
    month = datetime.date.today().month
    today = timezone.now().date()
    t = Order.objects.all().filter(date_orderd__date=today, complete=True, served=False)
    m = Order.objects.all().filter(date_orderd__month=month, complete=True, served=False)
    y = Order.objects.all().filter(date_orderd__year=year, complete=True, served=False)
    context = {
        't':t,
        'm':m,
        'y':y,
    }
    return render(request, 'sales.html', context) 

@login_required
def editSale(request, id):
    if request.method == 'POST':
        order = Order.objects.get(id=id)
        form = RecentSalesForm(request.POST, instance=order)

        if form.is_valid():
            form.save()

            return render(request, 'edit_sales.html', { 'form': form,'success': True})
    else:
        order = Order.objects.get(id=id)
        items = order.orderitem_set.all()
        tables = order.tableinfo_set.all()
        form = RecentSalesForm(instance=order)
    context = {
        'form': form,
        'order':order,
        'items':items,
        'tables':tables
    }
    return render(request, 'edit_sales.html', context)

def signUp(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = SignUpForm()


    context = {
        'form': form
    }

    return render(request, 'signup.html', context)

def changePassword(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #important
            messages.success(request, 'your password was successfully updated!')
            return render(request, 'change_password.html', {'success':True, 'form': form})
        else:
            messages.error(request, 'please correct the above errors!')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def staff(request):
    staffs = Staff.objects.all()

    context= {
        'staffs': staffs
    }
    return render(request, 'staff.html', context )

@login_required
def addStaff(request):
    if request.method == 'POST':
        form = AddStaffForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse('staff'))
    else:
        form = AddStaffForm()
    context = {
        'form': form
    }
    return render(request, 'add_staff.html', context)


@login_required
def editStaff(request, id):
    if request.method == 'POST':
        staff= Staff.objects.get(id=id)
        form = AddStaffForm(request.POST, instance=staff)

        if form.is_valid():
            form.save
            context= {
                'form': form,
                'staff': staff,
                'success': True
                }
            return render(request, 'edit_profile.html', context)
    else:
        staff= Staff.objects.get(id=id)
        form = AddStaffForm(instance=staff)

    context= {
                'form': form,
                'staff': staff
            }
    return render(request, 'edit_profile.html', context)
    
@login_required
def delete(request, id):
    staff = get_object_or_404(Staff, id=id)
    staff.delete()
    return redirect(reverse('staff'))

@login_required
def contacts(request):
    contacts = Contacts.objects.all()

    context = {
        'contacts': contacts
    }

    return render(request, 'contact_us.html', context)

@login_required
def editContactForm(request, id):
    if request.method == 'POST':
        contact= Contacts.objects.get(id=id)
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save
            return render(request, 'contact_details.html', {
                'contact':contact,
                'form': form,
                'success':True
                    })
    else:
        contact= Contacts.objects.get(id=id)
        form = ContactForm(instance=contact)

    context= {
        'contact':contact,
        'form': form,
            }
    return render(request, 'contact_details.html', context)


@login_required
def deleteContact(request, id):
    contacts = get_object_or_404(Contacts, id=id)
    contacts.delete()
    return redirect(reverse('contacts'))


@login_required
def staffDetails(request, id):
    staff= Staff.objects.get(id=id)
    context= {
        'staff':staff
    }
    return render(request, 'staff_details.html', context)

@login_required
def tableBooking(request):
    bookings = TableBooking.objects.all()

    context = {
        'bookings': bookings
    }

    return render(request, 'bookings.html', context)

@login_required
def deleteBooking(request, id):
    booking = get_object_or_404(TableBooking, id=id)
    booking.delete()
    return redirect(reverse('bookings'))

@login_required
def editBookingForm(request, id):
    if request.method == 'POST':
        booking= TableBooking.objects.get(id=id)
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save
            context= {
                'booking':booking,
                'form': form,
                'success':True
                }
            return render(request, 'booking_details.html', context)
    else:
        booking= TableBooking.objects.get(id=id)
        form = BookingForm(instance=booking)

    context= {
        'booking':booking,
        'form': form,
            }
    return render(request, 'booking_details.html', context)

@login_required
def review(request):
    reviews = CustomerReview.objects.all()

    context = {
        'reviews': reviews
    }

    return render(request, 'reviews.html', context)


def customerReview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'we highly appreciate your feedback')
            return redirect(reverse('index'))
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'customer_review.html', context)

@login_required
def editCustomerReview(request, id):
    if request.method == 'POST':
        review= CustomerReview.objects.get(id=id)
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save
        context= {
        'review':review,
        'form': form,
        'success': True
            }
        return render(request, 'review_details.html', context)
    else:
        review= CustomerReview.objects.get(id=id)
        form = ReviewForm(instance=review)

    context= {
        'review':review,
        'form': form,
            }
    return render(request, 'review_details.html', context)

@login_required
def deleteReview(request, id):
    review = get_object_or_404(CustomerReview, id=id)
    review.delete()
    return redirect(reverse('reviews'))

@login_required
def gallery(request):
    gallerys = Gallery.objects.all()
    context ={
        'gallerys': gallerys
    }
    return render(request, 'galleries.html', context)

@login_required
def editgallery(request, id):
    if request.method == 'POST':
        gallery= Gallery.objects.get(id=id)
        form = GalleryForm(request.POST, instance=gallery)

        if form.is_valid():
            form.save
        context= {
                'form': form,
                'success':True
            }
        return render(request, 'gallery_details.html', context)
    else:
        gallery= Gallery.objects.get(id=id)
        form = GalleryForm(instance=gallery)

    context= {
                'form': form,
            }
    return render(request, 'gallery_details.html', context)

@login_required
def deleteGallery(request, id):
    gallery = get_object_or_404(Gallery, id=id)
    gallery.delete()
    return redirect(reverse('galleries'))

@login_required
def events(request):
    events = Events.objects.all()
    context ={
        'events': events
    }
    return render(request, 'events.html', context)

@login_required
def deleteEvent(request, id):
    event = get_object_or_404(Events, id=id)
    event.delete()
    return redirect(reverse('events'))

@login_required
def editEvent(request, id):
    if request.method == 'POST':
        event= Events.objects.get(id=id)
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            form.save
        context= {
                'form': form,
                'success':True
            }
        return render(request, 'event_details.html', context)
    else:
        event= Events.objects.get(id=id)
        form = EventForm(instance=event)

    context= {
                'form': form,
            }
    return render(request, 'event_details.html', context)

@login_required
def company(request):
    infos = Company.objects.all()#correct this query to query on the last updated
    links = SocialMediaLink.objects.all()#correct this query to query on the last updated
    abouts = AboutUs.objects.all()#correct this query to query on the last updated
    context ={
        'infos': infos,
        'abouts':abouts,
        'links':links
    }
    return render(request, 'company.html', context)

@login_required
def editCompany(request, id):
    if request.method == 'POST':
        info= Company.objects.get(id=id)
        form = CompanyForm(request.POST, instance=info)

        if form.is_valid():
            form.save
        context= {
            'form': form,
            'info':info,
            'success':True
                }
        return render(request, 'company_details.html', context)
    else:
        info= Company.objects.get(id=id)
        form = CompanyForm(instance=info)

    context= {
                'form': form,
                'info':info
            }
    return render(request, 'company_details.html', context)

@login_required
def addLink(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('company'))
    else:
        form = LinkForm()
    context = {
        'form': form
    }
    return render(request, 'add_link.html', context)

@login_required
def editLink(request, id):
    if request.method == 'POST':
        link = SocialMediaLink.objects.get(id=id)
        form = LinkForm(request.POST, instance=link)

        if form.is_valid():
            form.save()

            return render(request, 'edit_link.html', { 'form': form,'success': True})
    else:
        link = SocialMediaLink.objects.get(id=id)
        form = LinkForm(instance=link)
    context = {
        'form': form,
    }
    return render(request, 'edit_link.html', context)

@login_required
def editAbout(request, id):
    if request.method == 'POST':
        about = AboutUs.objects.get(id=id)
        form = AboutForm(request.POST, instance=about)

        if form.is_valid():
            form.save()
            return render(request, 'edit_about.html', { 'form': form,'success': True})
    else:
        about = AboutUs.objects.get(id=id)
        form = AboutForm(instance=about)
    context = {
        'form': form
    }
    return render(request, 'edit_about.html', context)


@login_required
def addEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'add_event.html', {'form': form,'success':True})
    else:
        form = EventForm()
    context = {
        'form': form
    }
    return render(request, 'add_event.html', context)

@login_required
def addGallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'add_gallery.html', {'form': form,'success':True})
    else:
        form = GalleryForm()
    context = {
        'form': form
    }
    return render(request, 'add_gallery.html', context)


