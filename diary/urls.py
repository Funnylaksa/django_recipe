from django.urls import path

from diary.views import (
    DiaryCreateView,
    DiaryListView,
    DiaryDetailView,
    DiaryUpdateView,
    DiaryDeleteView
)

app_name = 'diary'
urlpatterns = [
    path('create/', DiaryCreateView.as_view(), name='create-view'),
    path('', DiaryListView.as_view(), name='list-view'),
    path('<int:id>/' ,DiaryDetailView.as_view(), name='detail-view'),
    path('<int:id>/update/', DiaryUpdateView.as_view(), name='update-view'),
    path('<int:id>/delete/', DiaryDeleteView.as_view(), name='delete-view')
]
