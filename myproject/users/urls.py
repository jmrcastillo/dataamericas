from django.urls import path
from . import views

urlpatterns = [
    path('pagesregister/', views.pagesregister_view, name='pagesregister'),
    path('pageslogin/', views.pageslogin_view, name='pageslogin'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
]