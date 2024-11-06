from django.contrib import admin

from .models import BasketballClub, StaffCurrent, Scoring

class BasketballClubAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'summary', 'companyId', 'approverId', 'status',
                    'createdDate', 'contactId', 'creatorType', 'addressId', 'comments'
                ]
admin.site.register(BasketballClub, BasketballClubAdmin)

class StaffCurrentAdmin(admin.ModelAdmin):
    list_display = ['id', 'staffId', 'position', 'level',
                    'clubId','status', 'dataCreated', 'comments'
                ]
admin.site.register(StaffCurrent, StaffCurrentAdmin)

class ScoringAdmin(admin.ModelAdmin):
    list_editable = ['attempts', 'accuracy', 'made' ]
    list_display = ['id', 'staffId', 'scoringType', 'locationType',
                    'clubId', 'creatorSaffId', 'attempts', 'made', 'accuracy', 'date', 'status'
                ]

admin.site.register(Scoring, ScoringAdmin)

# Register your models here.
