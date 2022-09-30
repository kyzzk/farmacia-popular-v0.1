from django.urls import path
from .views import home, my_logout, register_page


urlpatterns = [
    path('', home, name="home"),
    path('register/', register_page, name='register'),
    path('logout/', my_logout, name="logout"),
]