from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from .models import Post, Comment
from .forms import BlogPostForm, CommentForm

def get_posts(request):
	"""
	Create a view that will return a list 
	of posts that were published prior to 'now'
	and render them to the 'blogposts.html
	"""
	posts = Post.objects.filter(published_date__lte=timezone.now()
		).order_by('-published_date')
	return render(request, "blogposts.html", {'posts': posts})


# def post_detail(request, pk):
# 	"""
# 	Create a viw that returns a single
# 	Post object based on the post ID (pk) and
# 	render it to the 'postdetail.html' template.
# 	Or return a 404 error if the post is not found.
# 	"""
# 	post = get_object_or_404(Post, pk=pk)
# 	post.views += 1
# 	post.save()
# 	comments = Comment.objects.filter(active=True).order_by('-created_on')
# 	comment_form = CommentForm()
# 	return render(request, "postdetail.html", {'post': post, 
# 												'comments': comments,
# 												'comment_form': comment_form})


def post_detail(request, pk):
	template_name = "postdetail.html"
	post = get_object_or_404(Post, pk=pk)
	post.views += 1
	post.save()
	comments = Comment.objects.filter(active=True).order_by('-created_date')
	comment = None
	# Processing post requests
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			comment.post = post
			comment.owner = request.user
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		comment_form = CommentForm()

	return render(request, template_name, {'comment_form': comment_form, 
											'comment': comment,
											'comments': comments, 'post': post})

# def create_or_edit_post(request, pk=None):
#     """
#     Create a view that allows us to create
#     or edit a post depending if the Post ID
#     is null or not
#     """
#     post = get_object_or_404(Post, pk=pk) if pk else None
#     if request.method == "POST":
#         form = BlogPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post_detail, post.pk)
#     else:
#         form = BlogPostForm(instance=post)
#     return render(request, 'blogpostform.html', {'form': form})
