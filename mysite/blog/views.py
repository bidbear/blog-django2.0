from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator #导入分页器
from .models import Blog,BlogType

# Create your views here.
def blog_list(request):
    current_page = request.GET.get('page',1) #获取当前page的值，没有设置默认为1
    list_all = Blog.objects.all()   #取出所有数据
    paginator = Paginator(list_all,2) #分页器给数据分页，每页显示2条
    page_list = paginator.get_page(current_page) #验证，不在页码内返回第一页内容，超出页码返回最后一页内容
    current_num = page_list.number #获取当前页码
    all_page_num = paginator.num_pages #总页数
    #优化页码，获取当前页码的前后2页
    #max 和min 为了清除超出的页码
    page_range =list(range(max(current_num-2,1),current_num))+list(range(current_num,min(current_num+2,all_page_num)+1))
    #print(page_range)    [3,4,5,6,7]
    #在页码中添加...
    if page_range[0]-1 >=2:
        page_range.insert(0,'...')
    if all_page_num-page_range[-1] >=2:
        page_range.append('...')

    #在分页中添加首页和尾页
    if page_range[0] !=1:
        page_range.insert(0,1)
    if page_range[-1] != all_page_num:
        page_range.append(all_page_num)

    content = {}
    content['blogs'] = page_list
    content['current'] = int(current_page)   #需要把接受到的page的值转换为int类型
    content['page_range'] = page_range
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
