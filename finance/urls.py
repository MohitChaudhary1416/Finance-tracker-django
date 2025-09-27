from django.urls import path
from finance.views import RegisterView,DashboardView,TransactionCreateView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('transaction-add', TransactionCreateView.as_view(), name="transaction-add")

]