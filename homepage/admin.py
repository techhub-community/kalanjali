from django.contrib import admin
from .models import RegistrationModel
# # Register your models here.
#
#
details_fields = ['number','name','email','phone','college','year','event','coord_id','txn_id','amount']
display_fields = details_fields + ['verified',]
class UserAdmin(admin.ModelAdmin):
    list_display = display_fields
    search_fields = display_fields
    readonly_fields = details_fields
admin.site.register(RegistrationModel,UserAdmin)
