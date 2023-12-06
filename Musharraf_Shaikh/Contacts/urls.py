from django.urls import path
from .views import ContactListView, create_contact 
from .views import ContactListView, create_contact, ContactDetailView, ContactUpdateView  

urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", create_contact, name="contact_form"),  
    path("contacts/<int:pk>/", ContactDetailView.as_view(), name="contact_detail"),
    path("contacts/<int:pk>/update", ContactUpdateView.as_view(), name="contact_update"),
]