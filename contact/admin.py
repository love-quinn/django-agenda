from django.contrib import admin

# Register your models here.
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name','last_name', 'phone', 'category',
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = False
    list_display_links = 'id', 'phone',
    # list_editable = 'f irst_name', 'last_name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',