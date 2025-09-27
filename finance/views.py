from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login
from django.views import View
from finance.forms import RegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form = RegistrationForm()
        return render(request, 'finance/register.html', {'form':form})
    
    def post(self,request,*args,**kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
        
class DashboardView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        return render(request, 'finance/dashboard.html')
    
class TransactionCreateView(LoginRequiredMixin, View):
    def get(self,request,*args,**kwargs):
        return render(request, 'finance/transaction_form.html')
