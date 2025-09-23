
from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenBlacklistView , TokenObtainPairView , TokenRefreshSlidingView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("api.urls")),
    path("api/token/" , TokenObtainPairView.as_view() , name="get_token"),
    path("api/refresh/" , TokenRefreshSlidingView.as_view() , name="refresh")
]
