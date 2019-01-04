"""combocursos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from administracao import urls as administracao_urls
from usuarios import urls as usuarios_urls
from matriculas import urls as matriculas_urls
from cursos import urls as cursos_urls
from livros import urls as livros_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(administracao_urls), name='administracao'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('usuarios/', include(usuarios_urls), name='usuarios'),
    path('matriculas/', include(matriculas_urls), name='matriculas'),
    path('cursos/', include(cursos_urls), name='cursos'),
    path('livros/', include(livros_urls), name='livros'),
]
