from django.contrib import admin
from projects.models import Project, MyProjects, Ponds

# Register your models here.

class AllProjects(admin.ModelAdmin):
    list_display = ['name', 'summary', 'id']


class myProject(admin.ModelAdmin):
    list_display = ['position', 'projectId']


class AllPonds(admin.ModelAdmin):
    list_display = ['name', 'materialType', 'position_row', 'position_col']


class feedingCheck(admin.ModelAdmin):
    list_display = ['pondId', 'feedDateTime', 'quantity', 'reactions', 'size', 'AfeedDateTime']


admin.site.register(Project, AllProjects)
admin.site.register( MyProjects,myProject)
admin.site.register(Ponds, AllPonds)