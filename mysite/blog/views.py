from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType
# Create your views here.
def blog_list(request):
    content = {}
    content['blogs'] = Blog.objects.all()
    return render_to_response('blog/blog_list.html',content)

def blog_details(request,blog_id):
    content={}
    content['blog']=get_object_or_404(Blog,pk=blog_id)
    return render_to_response('blog/blog_details.html',content)
def blog_type(request,blog_type_id):
    content={}
    Blog_type = get_object_or_404(BlogType,pk=blog_type_id)
    content['blogs']=Blog.objects.filter(blog_type=Blog_type)
    content['blog_type']=Blog_type
    return render_to_response('blog/blog_type.html',content)