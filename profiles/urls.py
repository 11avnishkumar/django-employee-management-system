from django.urls import path
from profiles.views import (
    profile,
    profile_update_form,
)
urlpatterns = [
    path('', profile, name='employee-profile'),
    path('profile_update/', profile_update_form, name='profile_update'),
]