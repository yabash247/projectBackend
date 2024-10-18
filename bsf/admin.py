from django.contrib import admin

# Register your models here.
from .models import Batch, Laying

class BatchAdmin(admin.ModelAdmin):
    list_editable = ['farmId']
    list_display = ['id', 'farmId']
admin.site.register(Batch, BatchAdmin)

class LayingAdmin(admin.ModelAdmin):
    list_editable = ['batchId']
    list_display = ['id', 'batchId' ,'netId']
admin.site.register( Laying, LayingAdmin)