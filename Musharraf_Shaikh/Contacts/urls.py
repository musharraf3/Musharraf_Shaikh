from django.urls import path
from .views import ContactListView  # Import the create_contact view

urlpatterns = [
    path("", ContactListView.as_view(), name="contacts_list"),
]