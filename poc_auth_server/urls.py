from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from poc_auth_server.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),

    path('auth/token/', obtain_auth_token, name='token'),
]
