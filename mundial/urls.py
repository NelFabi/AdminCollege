"""
URL configuration for mundial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from album import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profesor/', views.ProfesorListView.as_view(), name='profesor-list'),
    # Update
    path('profesor/<int:pk>/update/',views.ProfesorUpdate.as_view(),name='profesor-update'), 
    #Create
    path('profesor/create/', views.ProfesorCreate.as_view(), name='profesor-create'),
    #Delete
    path('profesor/<int:pk>/delete/', views.ProfesorDelete.as_view(), name='profesor-delete'),

    path('materia/', views.MateriaListView.as_view(), name='materia-list'),
    # Update
    path('materia/<int:pk>/update/',views.MateriaUpdate.as_view(),name='materia-update'), 
    #Create
    path('materia/create/', views.MateriaCreate.as_view(), name='materia-create'),
    #Delete
    path('materia/<int:pk>/delete/', views.MateriaDelete.as_view(), name='materia-delete'),

    path('estudiante/', views.EstudianteListView.as_view(), name='estudiante-list'),
    # Update
    path('estudiante/<int:pk>/update/',views.EstudianteUpdate.as_view(),name='estudiante-update'), 
    #Create
    path('estudiante/create/', views.EstudianteCreate.as_view(), name='estudiante-create'),
    #Delete
    path('estudiante/<int:pk>/delete/', views.EstudianteDelete.as_view(), name='estudiante-delete'),
]
