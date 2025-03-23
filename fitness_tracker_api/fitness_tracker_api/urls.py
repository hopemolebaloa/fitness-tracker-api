from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include('activities.urls')),
        path('', include('goals.urls')),
    ])),
    path('api/token/', obtain_auth_token, name='api_token'),
]