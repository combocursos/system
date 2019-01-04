from django.contrib import admin
from .models import Livro


class LivroAdmin(admin.ModelAdmin):
    model = Livro
    list_display = ['nome']


admin.site.register(Livro, LivroAdmin)
