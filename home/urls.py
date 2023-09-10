from django.urls import path
from . import views

urlpatterns = [

path('', views.home, name='home'),
path('index/', views.index, name='index'),
path('addmoney/', views.addmoney, name='addmoney'),
path('profile/', views.profile, name='profile'),
path('profile_edit/', views.profile_edit, name='profile_edit'),
path('profile_update/', views.profile_update, name='profile_update'),

path('handleSignup/', views.handleSignup, name='handleSignup'),
path('handleLogin/', views.handleLogin, name='handleLogin'),
path('handleLogout/', views.handleLogout, name='handleLogout'),
path('addmoney_submission/', views.addmoney_submission, name='addmoney_submission'),
path('addmoney_update/', views.addmoney_update, name='addmoney_update'),

path('expense_edit/', views.expense_edit, name='expense_edit'),
path('expense_delete/', views.expense_delete, name='expense_delete'),


]



