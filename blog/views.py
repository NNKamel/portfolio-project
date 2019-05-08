from django.shortcuts import render, get_object_or_404

from .models import Blog
# Create your views here.
def allblogs(request):
    blog_objects = Blog.objects
    return render(request, 'blog/allblogs.html',{'blogs':blog_objects})


def detail(request, blog_id):
	detail_blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detailblog.html', {'blog':detail_blog})
