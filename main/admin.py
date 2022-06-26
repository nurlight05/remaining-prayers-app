from django.contrib import admin
from .models import Namaz

@admin.register(Namaz)
class NamazAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'code', 'view_remaining_prayers_count')
    
    def view_remaining_prayers_count(self, obj):
        return 0
    view_remaining_prayers_count.short_description = 'Remaining prayers'
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False