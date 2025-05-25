from django.urls import path
from .views import NoteListViews

urlpatterns = [
    path('notes_views/', NoteListViews.as_view())
]
