from django.contrib import admin
from .models import Time

class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'fundacao')
    list_filter = ('cidade',)
    search_fields = ('nome',)

admin.site.register(Time, TimeAdmin)
