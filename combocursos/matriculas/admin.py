from django.contrib import admin
from .models import Matricula
from .models import Dia
from .models import Turno
from .models import Horario
# Register your models here.

admin.site.register(Matricula)
admin.site.register(Dia)
admin.site.register(Turno)
admin.site.register(Horario)
