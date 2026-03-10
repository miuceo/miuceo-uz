from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import Post, PostImages, Comment, Projects
from django.contrib import messages

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all()[:5]
        context['projects']= Projects.objects.all()[:5]
        return context
    
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
    
class BlogPageView(ListView):
    template_name = 'blog.html'
    model = Post
    context_object_name = 'posts'
    
    
class SinglePostView(TemplateView):
    template_name = 'single-blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        post = Post.objects.get(slug=slug)
        context['post'] = post
        context['images'] = PostImages.objects.filter(post=post)
        return context
    
def add_comment(request, slug):
    if request.method == 'POST':
        post = Post.objects.get(slug=slug)
        content = request.POST.get('content')
        Comment.objects.create(post=post, content=content)

        messages.success(request, "Comment added successfully")

    return redirect('single-blog', slug=slug)
        
        
class ProjectsPageView(ListView):
    template_name = 'projects.html'
    model = Projects
    context_object_name = 'projects'
    
    
class ProjectDetailView(DetailView):
    template_name = 'single-project.html'
    model = Projects
    context_object_name = 'project'
    

class ContactPageView(TemplateView):
    template_name = 'contact.html'
    