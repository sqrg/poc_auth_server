from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from poc_auth_server.core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/token/', obtain_auth_token, name='token'),
    path('auth/register-device/', views.RegisterDevice.as_view(), name='register-device'),
]
