from django.contrib import admin
from .models import fichas

class ListandoFichas(admin.ModelAdmin):
    list_display = ('id', 'nome_ficha')
    list_display_links = ('id', 'nome_ficha')
    search_fields = ('nome_ficha',)
    list_filter = ('categoria',)
    list_per_page = 3

admin.site.register(fichas, ListandoFichas)
