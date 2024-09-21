from django.contrib import admin
from users.models import User,Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'id']


class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name' ,'verified']

admin.site.register(User, UserAdmin)
admin.site.register( Profile,ProfileAdmin)
