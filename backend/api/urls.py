
from django.urls import path , include
from .views import CreateUserView

urlpatterns = [
    path("api/user/register/" , CreateUserView.as_view() , name="register")
]
