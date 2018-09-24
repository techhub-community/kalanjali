from django.contrib import admin
from .models import RegistrationModel
# # Register your models here.
#
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','txn_id','event','verified')
    search_fields = ('name','email','phone','txn_id','event','verified')
    # readonly_fields = ('name','email','phone','txn_id','event',)
#
admin.site.register(RegistrationModel,UserAdmin)
