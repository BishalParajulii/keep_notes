
from django.urls import path , include
from .views import CreateUserView , NoteListCreate , NoteDelete

urlpatterns = [
    path("api/user/register/" , CreateUserView.as_view() , name="register"),
    path("notes/" , NoteListCreate.as_view() , name="note-list"),
    path("note/delete/<int:pk>/" , NoteDelete.as_view() , name="delete-note")
]
