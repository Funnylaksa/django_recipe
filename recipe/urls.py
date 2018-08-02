from django.urls import path
from recipe.views import recipe_delete_view, recipe_show_view, recipe_create_view, recipe_show_all_view, recipe_edit_view , recipe_random_view

app_name = 'recipe'
urlpatterns = [
    #path('show', recipe_show_view, name='list-view'),
    path('<int:id>' , recipe_show_view, name='detail-view'),
    path('<int:id>/edit', recipe_edit_view, name='edit-view'),
    path('create' , recipe_create_view, name='create-view'),
    path('<int:id>/delete' , recipe_delete_view, name='delete-view'),
    path('' , recipe_show_all_view, name='list-view'),
    path('random', recipe_random_view, name='random-view'),
]
