from django.urls import path, include
from accounts import views

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.user_profile, name="profile" ),
    path('password-reset/', include('accounts.url_reset'))
]