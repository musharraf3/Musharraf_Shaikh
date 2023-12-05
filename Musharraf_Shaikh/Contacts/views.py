from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Contacts

class ContactListView(ListView):
    model = Contacts
# Create your views here.


