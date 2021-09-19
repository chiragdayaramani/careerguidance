from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.home,name='home'),
    path('signup/',core_views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('after10/', core_views.after10, name='after10'),
    path('after12arts/', core_views.after12arts, name='after12arts'),
    path('after12science/', core_views.after12science, name='after12science'),
    path('after12commerce/', core_views.after12commerce, name='after12commerce'),
]
