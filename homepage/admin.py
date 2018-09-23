from django.contrib import admin
from .models import RegistrationModel
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','phone','txn_id','event','verified')
    search_fields = ('first_name','last_name','email','phone','txn_id','event','verified')

admin.site.register(RegistrationModel,UserAdmin)
