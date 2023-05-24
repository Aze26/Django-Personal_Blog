from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.html import strip_tags
import markdown
from django.db import models
from django.utils.six import python_2_unicode_compatible
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
class Tag(models.Model):
    name=models.CharField(max_length=100)
class Post(models.Model):
    title=models.CharField(max_length=70)#文章标题
    body=models.TextField()#文章正文
    created_time=models.DateTimeField()#文章创建时间
    modifield_time=models.DateTimeField()#文章修改时间
    excerpt=models.CharField(max_length=200,blank=True)#文章摘要
    category=models.ForeignKey(Category,on_delete=models.CASCADE)#文章分类
    tags=models.ManyToManyField(Tag,blank=True)#文章标签
    author=models.ForeignKey(User,on_delete=models.CASCADE)#文章作者
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    body=models.TextField()
    excerpt=models.CharField(max_length=200,blank=True)
    def save(self,*args,**kwargs):
        self.modified_time=timezone.now()
        md= markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args,**kwargs)
    
    
