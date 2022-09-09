from django.shortcuts import render
from django.views import generic
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"