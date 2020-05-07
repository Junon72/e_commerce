from django.urls import path
from . import views

urlpatterns = [
	path('', views.get_posts, name="get_posts"),
	# path('<pk>/detail/comment', views.post_comment, name='post_comment'),
	path('<pk>/', views.post_detail, name="post_detail")
]