from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Contact
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required
def home(request):
    contacts =Contact.objects.all()
    context ={'contacts':contacts, 'status':'We are currently working on this project','age':12}
    return render(request, 'app/index.html', context)

@login_required  
def detail(request, contact_id):
    contacts =get_object_or_404(Contact,pk=contact_id)
    context ={'contacts':contacts}
    return render(request,'app/detail.html', context)

class HomePageView(LoginRequiredMixin, ListView):
    template_name ='app/search.html'
    model =Contact
    context_object_name ='contacts'

    def get_queryset(self):
       contacts = super().get_queryset().filter(Manager = self.request.user)
       return contacts
       #or i can just write it like this contacts = super().get_queryset().filter(Manager = self.request.user)
       #return contacts

class ContactDetailsView(LoginRequiredMixin,DetailView):
    template_name = 'app/details.html'
    model = Contact
    context_object_name = 'contacts'
    

#@login_required
class SearchView(LoginRequiredMixin, ListView):
    template_name ='app/search.html'
    model =Contact
    context_object_name ='contacts'

@login_required
def search(request):
    if request.GET:
        search_term =request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(firstname__icontains= search_term) |
            Q(lastname__icontains = search_term) |
            Q(middlename__icontains= search_term) |
            Q(email__icontains= search_term) |
            Q(info__icontains = search_term) |
            Q(phone__iexact = search_term)
            #Q(status_active__iexact =search_term) | i am using the 'OR' for the search
            #Q(positin__iexact =search_term) |
            #Q(retired_active __iexact =search_term) |
            #Q(teacher__iexact =search_term)
            
            )
        context={
            'search_term':search_term,
            'contacts':search_results.filter(Manager =request.user) }
        return render(request, 'app/search.html', context)
    else:
        return redirect('home')

class ContactCreateViews(LoginRequiredMixin, CreateView):
    model =Contact
    template_name ='app/create.html'
    fields =['firstname', 'middlename','lastname','email','phone','info','gender','image','image']
    success_url ='home/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.Manager =self.request.user
        instance.save()
        messages.success(self.request,'Congatulations!!, Your contact has been saved successfully')
        return redirect('/home')

class ContactUpdateViews(LoginRequiredMixin, UpdateView):
    model =Contact
    fields =['firstname', 'middlename','lastname','email','phone','info','gender','image','image']
    template_name ='app/update.html'
    
    def form_valid(self, form):
        instance =form.save()
        messages.success(self.request,'Congatulations!!, Your contact has been successfully updated')
        return redirect('detail', instance.pk)


class ContactDeleteView(LoginRequiredMixin,DeleteView):
    model = Contact
    template_name ='app/delete.html'
    success_url ='/home'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'You have finally deleted the contact!')
        return super().delete(self, request, *args, **kwargs)

class SignUpView(CreateView):
    form_class =UserCreationForm
    template_name ='registration/signup.html'
    success_url ='/home/'