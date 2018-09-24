from django.contrib import admin
from .models import RegistrationModel
# # Register your models here.
#
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','college','event','txn_id','verified')
    search_fields = ('name','email','phone','college','event','txn_id','verified')
    # readonly_fields = ('name','email','phone','txn_id','event',)
#
admin.site.register(RegistrationModel,UserAdmin)
