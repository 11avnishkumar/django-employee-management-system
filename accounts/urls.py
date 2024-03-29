from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import *
urlpatterns = [
    path('signin/', signIn,name='signin'),
    path('signup/', signUp,name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/signin.html'), name='logout'),
]