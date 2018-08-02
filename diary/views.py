from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Diary
# Create your views here.
class DiaryListView(View):
    template_name = "diary/diary_list.html"
    queryset=Diary.objects.all()

    def get(self,request,*args,**kwargs):
        print (Diary.objects.all())
        context = {'object_list':self.queryset}
        return render (request, self.template_name, context)


class DiaryView(View):
    template_name = "diary/diary_detail.html"
    def get(self,request,id=None,*args,**kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Diary, id=id)
            context = {'object':obj}
        return render (request, self.template_name, context)
