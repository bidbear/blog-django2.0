# blog-django2.0
## 按照b站上教程做的博客网站 [网址](https://space.bilibili.com/252028233?spm_id_from=333.788.b_765f7570696e666f.2)
> ### 分页的实现
> * 分页效果用的django2.0自带的 分页器。使用的话可以问度娘
> * 分页的视图层地址 [链接](https://github.com/bidbear/blog-django2.0/blob/master/mysite/blog/views.py)
> * 分页的模版页实现 [链接](https://github.com/bidbear/blog-django2.0/blob/master/mysite/blog/templates/blog/blog_list.html)

### 分页器常用方法
```
  ### Paginator创建一个分页对象
    current_page = request.GET.get('p')

    paginator = Paginator(L, 10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象


  ### 指定页数，获取当夜对象
    posts = paginator.page(1) 
    # has_next              是否有下一页
    # next_page_number      下一页页码
    # has_previous          是否有上一页
    # previous_page_number  上一页页码
    # object_list           分页之后的数据列表
    # number                当前页
    # paginator             paginator对象
```
### 配置后台富文本编辑器
> * 安装富文本编辑器应用 `pip install django-ckeditor`
> * 注册ckeditor应用
> * 修改model 
   ```
    from ckeditor.fields import RichTextField
    content = RichTextField()
   ```
> * 启动后台发现是繁体字，修改 setting `LANGUAGE_CODE = 'zh-hans'`
> #### 富文本上传图片
> *  安装图片处理依赖 `pip install pillow`
> * 注册ckeditor_uploader应用
> * 配置settings 
```
    MEDIA_URL = '/media/'
    # 放在django项目根目录，同时也需要创建media文件夹
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    CKEDITOR_UPLOAD_PATH = 'upload/'
```
> * 配置上传url和media的访问,打开全局url.py 
```
    path('ckeditor/', include('ckeditor_uploader.urls')),
    另外，上传的图片是到media中，不是在static中。我们还需要设置media可被访问，如下设置可用于开发中使用，若部署到服务器可用服务器软件设置：
    from django.conf import settings
    from django.conf.urls.static import static
    ...
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
> * 修改model 
```
  from ckeditor_uploader.fields import RichTextUploadingField
  ...
  content = RichTextUploadingField()
  
```
