from django.urls import path
from . import views
      
urlpatterns = [  
    path('', views.home, name='home'),
    path('stores/', views.store_list, name='store-list'),
    path('stores/<int:pk>/', views.store_detail, name='store-detail'),
    path('stores/cretae/', views.store_create, name='store-create'),
    path('stores/<int:pk>/update/', views.store_update, name='store-update'),
    path('stores/<int:pk>/delete/', views.store_delete, name='store-delete'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]