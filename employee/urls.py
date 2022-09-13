from django.urls import path
from django.contrib.auth import views as auth_views
from employee.views import (
    home_page_view,
    employee_detail_view,
    add_employee_view,
    update_employee_view,
    inactive_employee,
    upload_file_view,
)
urlpatterns = [
    path('', home_page_view, name='home-page'),
    path('view_employee/<slug:employee_slug>/', employee_detail_view, name='employee-details'),
    path('new_employee/', add_employee_view, name='add-employee'),
    path('new_employee/upload/', upload_file_view, name='add-employee-upload'),
    path('update_employee_details/<int:id>/change', update_employee_view, name='update-employee'),
    path('inactive_employee_details/<int:id>/inactive', inactive_employee, name='inactive-employee'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
]