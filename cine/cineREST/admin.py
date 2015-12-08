from django.contrib import admin
from cineREST.models import Film

# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'on_screen')

admin.site.register(Film, FilmAdmin)