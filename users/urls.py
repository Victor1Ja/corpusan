from django.urls import path, include
from . import views
from django.contrib.auth import views as djangoViews
app_name = 'users'

urlpatterns = [
    path('', views.user, name = 'user'),
    #path('register/', views.register, name = 'register'),
    path('login/', djangoViews.LoginView.as_view(template_name = 'users/login.html') , name = 'login'),
    path('logout/', views.logout_view , name = 'logout'),
]