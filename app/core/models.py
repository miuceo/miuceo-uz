from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'posts'
        
        
class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')
    
    def __str__(self):
        return f"Image for {self.post.title}"
    
    class Meta:
        verbose_name = 'Post Image'
        verbose_name_plural = 'Post Images'
        db_table = 'post_images'
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment for {self.post.title}"
    
    class Meta:
        ordering = ['created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comments'
             
             
class Projects(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Projects.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'projects'
        

class ProjectImages(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')
    
    def __str__(self):
        return f"Image for {self.project.title}"
    
    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'
        db_table = 'project_images'