from django.urls import path
from .views import (
    home, store_list, store_detail, store_create, store_update, store_delete,
    signup_view, login_view, logout_view, about_view, contact_view, add_favorite, remove_favorite
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('stores/', store_list, name='store-list'),
    path('stores/<int:pk>/', store_detail, name='store-detail'),
    path('stores/create/', store_create, name='store-create'),
    path('stores/<int:pk>/update/', store_update, name='store-update'),
    path('stores/<int:pk>/delete/', store_delete, name='store-delete'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('favorite/add/<int:store_id>/', add_favorite, name='add_favorite'),
    path('favorite/remove/<int:store_id>/', remove_favorite, name='remove_favorite'),
]
