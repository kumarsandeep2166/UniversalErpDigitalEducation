from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Course


class CourseList(ListView):
    pass
class CourseCreateView(CreateView):
    pass
class CourseDetailView(DetailView):
    pass
class CourseUpdateView(UpdateView):
    pass
class CourseDeleteView(DeleteView):
    pass