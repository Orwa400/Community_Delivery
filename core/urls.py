from django.urls import path
from .views import  home, store_list, store_detail, store_create, store_update, store_delete, signup_view 
from . import views


urlpatterns = [  
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('stores/', views.store_list, name='store-list'),
    path('stores/<int:pk>/', views.store_detail, name='store-detail'),
    path('stores/create/', views.store_create, name='store-create'),
    path('stores/<int:pk>/update/', views.store_update, name='store-update'),
    path('stores/<int:pk>/delete/', views.store_delete, name='store-delete'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]