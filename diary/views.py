from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
    )

from .models import Diary
from .forms import DiaryModelForm
# Create your views here.

class DiaryCreateView(CreateView):
    template_name = 'diary/diary_create.html'
    form_class = DiaryModelForm
    queryset = Diary.objects.all() #<app>/<model>_<generic view>.html

    def form_valid(self,form):
        print (form.cleaned_data)
        return super().form_valid(form)

class DiaryListView(ListView):
    queryset = Diary.objects.all()

class DiaryDetailView(DetailView):
    template_name = "diary/diary_detail.html"
    def get_object(self):
        id = self.kwargs.get('id')
        return (get_object_or_404(Diary, id=id))

class DiaryUpdateView(UpdateView):
    template_name = 'diary/diary_create.html'
    form_class = DiaryModelForm

    def get_object(self):
        id=self.kwargs.get('id')
        return (get_object_or_404(Diary, id=id))

    def form_valid(self,form):
        print (form.cleaned_data)
        return super().form_valid(form)

class DiaryDeleteView(DeleteView):
    template_name = 'diary/diary_delete.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return (get_object_or_404(Diary, id=id_))

    def get_success_url(self):
        return reverse('diary:list-view')
