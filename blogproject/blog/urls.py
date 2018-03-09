from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetaileView.as_view(),name='detail'),
    url(r'^achives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$',views.AchivesView.as_view(),name='achives'),
    url(r'category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
]
