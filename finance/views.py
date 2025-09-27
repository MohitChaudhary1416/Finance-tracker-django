from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login
from django.views import View
from finance.forms import RegistrationForm,TransactionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from finance.models import Transaction

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
        return render(request, 'finance/register.html', {'form':form})
    
        
class DashboardView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        return render(request, 'finance/dashboard.html')
    
class TransactionCreateView(LoginRequiredMixin, View):
    def get(self,request,*args,**kwargs):
        form = TransactionForm()
        return render(request, 'finance/transaction_form.html', {'form':form})
    
    def post(self,request,*args,**kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
        
        return render(request, 'finance/transaction_form.html', {'form':form})


class TransactionListView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        transactions = Transaction.objects.all()
        return render(request, 'finance/transaction_list.html',{'transactions':transactions} )


        
    
