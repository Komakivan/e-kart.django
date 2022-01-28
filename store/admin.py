from django.contrib import admin
from .models import Product


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	list_display =('product_name','price','stock','category','is_available','created_date','modified_date')
	prepopulated_fields ={'slug': ('product_name',)}

	filter_horizontal =()
	list_filter=()
	fieldsets =()


 

admin.site.register(Product,ProductAdmin)