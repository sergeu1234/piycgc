from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('contact.html',views.contact, name= 'contact'),
    path('about.html',views.about, name= 'about'),
    path('services.html',views.services, name= 'services'),
    path('pricing.html',views.pricing, name= 'pricing'),
    path('opening-hour.html',views.opening_hour, name= 'opening_hour'),
    path('blog_home.html',views.blog_home, name= 'blog_home'),
    path('blog_single.html',views.blog_single, name= 'blog_single'),
    
] 