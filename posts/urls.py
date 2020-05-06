from django.urls import path, include
from . import views
urlpatterns = [
	path('', views.get_posts, name="get_posts"),
	path('<int:pk>/', views.post_detail, name="post_detail")
]