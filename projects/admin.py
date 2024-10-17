from django.contrib import admin
from projects.models import Project, MyProjects, Ponds, PondstoDoList, Stocking, Company

# Register your models here.

class AllProjects(admin.ModelAdmin):
    list_display = ['name', 'summary', 'id']


class myProject(admin.ModelAdmin):
    list_display = ['position', 'projectId']


class AllPonds(admin.ModelAdmin):
    list_display = ['id','name', 'materialType', 'position_row', 'position_col']


class feedingCheck(admin.ModelAdmin):
    list_display = ['pondId', 'feedDateTime', 'quantity', 'reactions', 'size', 'AfeedDateTime']


class ToDoListP(admin.ModelAdmin):
    list_display = ['pondId', 'farmId', 'pomdName', 'taskName', 'taskId', 'urgency', 'assignedToId', 'taskDetails' ]


admin.site.register(Project, AllProjects)
admin.site.register( MyProjects,myProject)
admin.site.register(Ponds, AllPonds)
admin.site.register(PondstoDoList, ToDoListP)

class StockingAdmin(admin.ModelAdmin):
    list_display = ['id', 'pondId', 'totalWeight',  'quantity', 'comments']

admin.site.register(Stocking, StockingAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'creatorId',  'City', 'comments']

admin.site.register(Company, CompanyAdmin)