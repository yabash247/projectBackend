from django.contrib import admin

# Register your models here.
from .models import Batch, Net, NetStat, Container, ContainerStat, Authority, StaffCurrent, StaffOrgChart, Farm

class AuthorityAdmin(admin.ModelAdmin):
    list_display = ['id', 'tableName', 'farmId', 'view', 'add', 'edit',
                    'delete','accept', 'approve'
                ]
admin.site.register(Authority, AuthorityAdmin)

class FarmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'summary', 'companyId', 'approverId', 'status',
                    'createdDate', 'contactId', 'ownerType', 'addressId', 'comments'
                ]
admin.site.register(Farm, FarmAdmin)

class StaffCurrentAdmin(admin.ModelAdmin):
    list_display = ['id', 'staffId', 'position', 'level', 'pay',
                    'farmId','status', 'dataCreated', 'comments'
                ]
admin.site.register(StaffCurrent, StaffCurrentAdmin)

class StaffOrgChartAdmin(admin.ModelAdmin):
    list_editable = ['creatorSaffId', 'approvalSaffId']
    list_display = ['id', 'staffId', 'bossId', 'startDate', 'creatorSaffId', 'approvalSaffId',
                    'endDate','status'
                ]
admin.site.register(StaffOrgChart, StaffOrgChartAdmin)

class BatchAdmin(admin.ModelAdmin):
    list_editable = ['farmId']
    list_display = ['id', 'farmId']
admin.site.register(Batch, BatchAdmin)

class NetAdmin(admin.ModelAdmin):
    list_editable = ['netNumber']
    list_display = ['id', 'farmId' ,'netNumber']
admin.site.register( Net, NetAdmin)

class NetStatusAdmin(admin.ModelAdmin):
    list_editable = ['netNumber', 'batchNumber']
    list_display = ['id', 'batchNumber' ,'netNumber', 'status', 'eggiesSetDate', 'eggiesRemovedDate', 'eggiesHarvested']
admin.site.register( NetStat, NetStatusAdmin)

class ContainerAdmin(admin.ModelAdmin):
    #list_editable = ['containerType', 'name']
    list_display = ['id', 'farmId' ,'containerName', 'containerType', 'containerUse']
admin.site.register( Container, ContainerAdmin)

class ContainerStatAdmin(admin.ModelAdmin):
    list_editable = ['batchNumber', 'containerNumber']
    list_display = ['id', 'batchNumber' ,'containerNumber', 'status', 'harveststage', 'setDate', 'removedDate', 'harvestWeight']
admin.site.register( ContainerStat, ContainerStatAdmin)

