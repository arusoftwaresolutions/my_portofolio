from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    date_hierarchy = 'created_at'
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')
