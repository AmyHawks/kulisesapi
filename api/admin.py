from django.contrib import admin
from .models import Show, Director, Actor, Theatre


# Register your models here.
@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'price', 'season', 'language']
    list_editable = ['duration', 'price']
    list_per_page = 10


admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Theatre)
