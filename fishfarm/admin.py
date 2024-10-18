from django.contrib import admin

# Register your models here.
from .models import Authority, Staff, StaffCurrent, StaffOrgChart

class AuthorityAdmin(admin.ModelAdmin):
    list_display = ['id', 'tableName', 'view', 'add', 'edit',
                    'delete','accept', 'approve'
                ]
admin.site.register(Authority, AuthorityAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'userId', 'companyId', 'workPhone',
                    'dataCreated','joinedCompanyDate', 'comments'
                ]
admin.site.register(Staff, StaffAdmin)

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
