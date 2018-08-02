from django.urls import path
from .views import DiaryView, DiaryListView

app_name = 'diary'
urlpatterns = [
    path('' , DiaryListView.as_view(template_name='diary/diary_list.html'), name='list-view'),
    path('<int:id>', DiaryView.as_view(), name='detail-view')
]
