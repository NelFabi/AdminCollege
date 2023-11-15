from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Profesor, Materia, Estudiante

# Create your views here.
class ProfesorListView(ListView):
    model = Profesor

class ProfesorUpdate(UpdateView):
    model = Profesor
    fields = '__all__' 

class ProfesorCreate(CreateView):
    model = Profesor
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('profesor-list')

class ProfesorDelete(DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesor-list')

class MateriaListView(ListView):
    model = Materia

class MateriaUpdate(UpdateView):
    model = Materia
    fields = '__all__' 

class MateriaCreate(CreateView):
    model = Materia
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('materia-list')

class MateriaDelete(DeleteView):
    model = Materia
    success_url = reverse_lazy('materia-list')

class EstudianteListView(ListView):
    model = Estudiante

class EstudianteUpdate(UpdateView):
    model = Estudiante
    fields = '__all__' 

class EstudianteCreate(CreateView):
    model = Estudiante
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('estudiante-list')

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante-list')