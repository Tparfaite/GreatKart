from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','joined_date','last_login','is_active')
    list_display_links=('email','last_name','first_name')
    readonly_fields=('last_login','joined_date')
    ordering=('joined_date',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Account, AccountAdmin)

