"""
URL configuration for Cost_automation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Managed_services import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view ,name='login'),
    path('home/', views.home ,name='home'),
    path('Newform/', views.scoping_form ,name='new_form'),
    path('ModifyForm/', views.modify_form, name='modify_form'), 
    path("export_data/", views.export_all_data, name="export_all_data"),
    path('fetch_project_data/', views.fetch_project_data, name='fetch_project_data'),
    path('implementation/', views.implement, name='implement'),
    path('reports/', views.reports, name='reports'),
     path('export_table/', views.export_report_table, name='export_table'),

    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', views.logout_view, name='logout'),


    # Password Reset Views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    

]

