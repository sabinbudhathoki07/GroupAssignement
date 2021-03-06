"""OpenTender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from Tender import views

admin.site.site_header = "Open Tender Admin Dashboard"
admin.site.site_title = "Open Tender Admin Dashboard"
admin.site.index_title = "Open Tender Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login),
    path('signup',views.signup),
    path('entry', views.entry),
    path("dashboard", views.dashboard),
    path('tender',views.tender),
    path('aboutus',views.aboutus),
    path('faq',views.faq),
    path('moreinformation/<int:id>',views.moreinformation),
    path('apply',views.apply),
    path("upload",views.upload),
    path('post_edit/<int:id>',views.post_edit),
    path('update/<int:id>',views.post_update),
    path('delete/<int:id>',views.post_delete),
    
    path('delete_user/<int:id>',views.user_delete),
    path('application/<int:id>',views.application),
    path("edit_account/<int:id>",views.account_edit),
    path('update_user/<int:id>',views.update_user),
    path("logout",views.logout),
]
