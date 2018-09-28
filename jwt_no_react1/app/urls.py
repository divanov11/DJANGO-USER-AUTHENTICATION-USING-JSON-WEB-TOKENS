from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('get_token/', obtain_auth_token, name="get_token"),

    path('get_user/<slug:key>/', views.user, name="get_user"),
]
