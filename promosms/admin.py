from django.contrib import admin
from .models import PromoSmsModel

# Register your models here.
data_list = ['phone','sms_sent']
class UserAdmin(admin.ModelAdmin):
    list_display = data_list
    search_fields = data_list
    readonly_fields = data_list

admin.site.register(PromoSmsModel,UserAdmin)
