from django.contrib import admin
from finance.models import Transaction
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    class Meta:
        model = Transaction
        list_display = ['user', 'title', 'amount', 'transation_type','date', 'category']