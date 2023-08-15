from django.contrib import admin
from .models import Worker, PlantsModel
# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'salary')
@admin.register(PlantsModel)
class PlantsModelAdmin(admin.ModelAdmin):
    list_display = ('plants_name', 'plants_amount', 'purchase_date', 'price')
