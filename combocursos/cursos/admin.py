from django.contrib import admin
from .models import Curso


class CursoAdmin(admin.ModelAdmin):
    model = Curso
    list_display = ['nome', 'periodo']


admin.site.register(Curso, CursoAdmin)
