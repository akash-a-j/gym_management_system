from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.handlelogin,name="handlelogin"),
    path('logout/',views.handleLogout,name="handleLogout"),
    path('contact/',views.contact,name="contact"),
    path('join/',views.enroll,name="enroll"),
    path('profile/',views.profile,name="profile"),
    path('gallery/',views.gallery,name="gallery"),
    path('attendance/',views.attendance,name="attendance"),
    path('trainer/',views.trainer,name="trainer"),
    path('products/', views.product_list, name="product_list"),  # Show all products
    path('products/<int:category_id>/', views.product_list, name="product_list_by_category"),  # Show products by category
    path('product/<int:product_id>/', views.product_detail, name="product_detail"),  # Show product detail
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/trainers/', views.manage_trainers, name='manage_trainers'),
    path('dashboard/trainers/add/', views.trainer_add, name='trainer_add'),
    path('dashboard/trainers/edit/<int:pk>/', views.trainer_edit, name='trainer_edit'),
    path('dashboard/trainers/delete/<int:pk>/', views.trainer_delete, name='trainer_delete'),
    path('dashboard/gallery/', views.manage_gallery, name='manage_gallery'),
    path('dashboard/gallery/delete/<int:pk>/', views.gallery_delete, name='gallery_delete'),
    path('dashboard/products/', views.manage_products, name='manage_products'),
    path('dashboard/products/add/', views.product_add, name='product_add'),
    path('dashboard/products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('dashboard/products/delete/<int:pk>/', views.product_delete, name='product_delete'),

]
