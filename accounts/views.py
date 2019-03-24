from django.shortcuts import render

# May need to adjust this. not sure if it will work
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

# Grabbing forms from current directory
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'