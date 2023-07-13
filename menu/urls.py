from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('menu/', views.menu , name='menu'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('new_menu/', views.newMenu , name='new_menu'),
    path('add_category/', views.addCategory , name='add_category'),
    path('best_time/', views.addBestTime , name='add_best'),
    path('edit_menu/<int:id>', views.editMenu, name='edit_menu'),
    path('customers/', views.customers , name='customers'),
    path('<int:id>/delete_customer/', views.deleteCustomer, name='delete_customer'),
    path('cart/', views.cart , name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('contact_us/', views.contactUs, name='contact_us'),
    path('book_table/', views.bookTable, name='book_table'),
]