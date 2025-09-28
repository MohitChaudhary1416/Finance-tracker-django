from django.contrib import admin
from finance.models import Transaction,Goal
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    class Meta:
        model = Transaction
        list_display = ['user', 'title', 'amount', 'transation_type','date', 'category']

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    class Meta:
        model = Goal
        list_display = ['user','name','target_amount','deadline','current_amount']


