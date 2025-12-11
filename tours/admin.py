from django.contrib import admin
from .models import Tour

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'popularity', 'destination_type')
    list_filter = ('destination_type', 'duration')
    search_fields = ('name', 'description', 'tags')