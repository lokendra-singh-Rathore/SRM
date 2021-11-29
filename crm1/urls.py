

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.About,name='about'),
    path('duplo/',views.duplo,name='duplo'),
    path('wedo/',views.wedo,name='wedo'),
    path('nxt/',views.nxt,name='nxt'),
    path('ev3/',views.ev3,name='ev3'),
    path('electronics/',views.electronics,name='electronics'),
    path('arduino/',views.arduino,name='arduino'),
    path('pi/',views.pi,name='pi'),
    
    path('gallery/',views.gallery,name='gallery'),
    
    path('acc', include('accounts.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
	url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]
