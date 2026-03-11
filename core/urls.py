from django.urls import path
from .views import HomePageView, AboutPageView, BlogPageView, SinglePostView, add_comment, ProjectsPageView, ProjectDetailView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('blog/<slug:slug>/', SinglePostView.as_view(), name='single-blog'),
    path('blog/<slug:slug>/comment', add_comment, name='comment'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='single-project'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
