from django.contrib import admin
from Myaccount.models import Accounts
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
	list_display =['email','first_name','last_name','username','date_joined','last_login','is_active']

	filter_horizontal =()
	list_filter=()
	fieldsets=()

admin.site.register(Accounts,AccountAdmin)

