from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('view_expenses/', views.view_expenses, name='view_expenses'),
    path('summary/', views.summary, name='summary'),
    path('sign_up/', views.sign_up, name='sign_up'),
]
