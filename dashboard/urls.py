from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . forms import LoginForm

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sales/', views.sales, name='sales'),
    path('sale_details/<int:id>/', views.editSale, name='edit_sale'),
    path('signup/', views.signUp, name ='signup'),
    path('change_password/', views.changePassword, name ='change_password'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(), name ='logout'),
    path('contacts/', views.contacts, name ='contacts'),
    path('contact_details/<int:id>/', views.editContactForm, name='contact_details'),
    path('staff/', views.staff, name ='staff'),
    path('staff/<int:id>/edit_profile/', views.editStaff, name='edit_profile'),
    path('staff/<int:id>/delete/', views.delete, name='delete_staff'),
    path('contact/<int:id>/delete/', views.deleteContact, name='delete_contact'),
    path('add_staff/', views.addStaff, name='add_staff'),
    path('edit_staff/<int:id>/', views.editStaff, name='edit_staff'),
    path('staff_details/<int:id>/', views.staffDetails, name ='staff_details'),
    path('bookings/', views.tableBooking, name ='bookings'),
    path('booking/<int:id>/delete/', views.deleteBooking, name='delete_booking'),
    path('booking_details/<int:id>/', views.editBookingForm, name='booking_details'),
    path('reviews/', views.review, name ='reviews'),
    path('customer_review/', views.customerReview, name ='review'),
    path('review_details/<int:id>/', views.editCustomerReview, name='review_details'),
    path('review/<int:id>/delete/', views.deleteReview, name='delete_review'),
    path('galleries/', views.gallery, name ='galleries'),
     path('add_gallery/', views.addGallery, name='add_gallery'),
    path('gallery_details/<int:id>/', views.editgallery, name='gallery_details'),
    path('gallery/<int:id>/delete/', views.deleteGallery, name='delete_gallery'),
    path('events/', views.events, name ='events'),
     path('add_event/', views.addEvent, name='add_event'),
    path('event/<int:id>/delete/', views.deleteEvent, name='delete_event'),
    path('event_details/<int:id>/', views.editEvent, name='event_details'),
    path('company/', views.company, name ='company'),
    path('company_details/<int:id>/', views.editCompany, name='company_details'),
    path('add_link/', views.addLink, name='add_link'),
    path('link_details/<int:id>/', views.editLink, name='edit_link'),
    path('edit_about/<int:id>/', views.editAbout, name='edit_about'),

]