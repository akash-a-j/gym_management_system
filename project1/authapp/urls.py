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

]
