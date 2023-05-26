from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.addNote, name="addNote"),
    path('<int:note_id>/', views.viewNote, name="viewNote"),
    path('<int:note_id>/delete/', views.deleteNote, name="deleteNote"),
    path('<int:note_id>/edit/', views.editNote, name="editNote")
]