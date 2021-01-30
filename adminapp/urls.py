from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.UsersListView.as_view(), name='admin_users'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', adminapp.UserDeleteView.as_view(), name='admin_users_remove'),
    path('products/', adminapp.ProductsListView.as_view(), name='admin_products'),
    path('products/create/', adminapp.ProductCreateView.as_view(), name='admin_products_create'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='admin_products_update'),
    path('products/remove/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='admin_products_remove'),
]
