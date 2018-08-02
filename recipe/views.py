from django.shortcuts import render,redirect, get_object_or_404

from .forms import RecipeForm,RawRecipeForm
from .models import Recipe

from django.http import HttpResponseRedirect
import random


# Create your views here.
#create that works
"""
def recipe_create_view(request , *args, **kwargs):
    form=RecipeForm(request.POST or None)
    if form.is_valid():
        form=RecipeForm(request.POST, request.FILES)
        print (request.POST.keys()) # gets text key fields
        print (request.FILES.keys()) # gets image fields
        form.save()
        #file=Recipe(picture=request.FILES['picture'])
        #file.save()
        return HttpResponseRedirect('/show/')

    context = {'form':form} #, uploaded_file_url': uploaded_file_url}
    return render(request, 'recipe_create.html' , context)
"""
def recipe_show_all_view(request, *args , **kwargs):
    context = {'objects':Recipe.objects.all()}
    return render(request, 'recipe_show_all.html' , context)

                # POST gets text key fields
                # FILES gets image fields
                # form=RecipeForm(request.POST, request.FILES)
                # form.save()
def recipe_create_view(request , *args, **kwargs):
    my_form=RawRecipeForm()
    if request.method == 'POST':
        my_form=RawRecipeForm(request.POST,request.FILES)
        if my_form.is_valid():
            print (my_form.cleaned_data)
            Recipe.objects.create(**my_form.cleaned_data)
            return redirect('/recipe/')#+str(obj.id))
    context = {'form':my_form} #, uploaded_file_url': uploaded_file_url}
    return render(request, 'recipe_create.html' , context)

def recipe_show_view(request, id=1, *args , **kwargs):
    #use latest id if id is invalid
    try:
        Recipe.objects.get(id=id)
    except:
        id = Recipe.objects.latest('id').id
    print (id)
    #obj = get_object_or_404(Recipe, id = id)
    obj = Recipe.objects.get(id=id)
    #next_obj = Recipe.objects.get_next_by_datetime()
    next_obj = Recipe.objects.filter(id__gt=id).order_by('id').first()
    prev_obj = Recipe.objects.filter(id__lt=id).order_by('id').last()
    print (next_obj)
    print (prev_obj)
    if next_obj==None:
        next_obj = Recipe.objects.filter(id__lt=id).order_by('id').first()
    if prev_obj ==None:
        prev_obj = Recipe.objects.filter(id__gt=id).order_by('id').last()
    context = {'object':obj, 'next_obj':next_obj, 'prev_obj':prev_obj}
    return render(request, 'recipe_show.html' , context)

def recipe_edit_view(request, id , *args, **kwargs):
    obj = Recipe.objects.get(id=id)
    my_form=RecipeForm(instance=obj)
    if request.method =='POST':
        print (request.POST.get('edit'))
        my_form=RecipeForm(request.POST,request.FILES,instance=obj)
        if my_form.is_valid():
            my_form.save()
            return redirect('/recipe/')
    context={'form':my_form}
    return render(request,'recipe_create.html',context)

def recipe_delete_view(request, id , *args, **kwargs):
    obj = get_object_or_404(Recipe, id=id)
    print (obj)
    print (request.method)
    if request.method =='POST':
        obj.delete()
        print ('it works?')
        return redirect('/recipe/')
    context={'object':obj}
    return render(request,'recipe_delete.html',context)

def recipe_random_view(request,*args,**kwargs):
    obj = random.choice(Recipe.objects.all())
    print (obj)
    context = {'object':obj}
    return redirect('/recipe/'+str(obj.id))
    #return render(request, 'recipe_show.html',context)
