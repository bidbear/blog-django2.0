from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
#博客类型
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name
#博客内容
class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete = models.DO_NOTHING)
    author = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_time']    

    def __str__(self):
        return self.title

