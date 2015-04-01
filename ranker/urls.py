from django.conf.urls import patterns, url
from ranker import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'ranker/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'ranker/logout.html',
         'next_page': 'index'}, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^create_project/$', views.create_project, name='create_project'),
    url(r'^view_project/(?P<project_id>\d+)$', views.view_project, name='view_project'),
    url(r'^vote/(?P<project_id>\d+)/(?P<item1_id>\d+)/(?P<item2_id>\d+)/(?P<value>0|1)$', views.vote, name='vote'),
    url(r'^rate/(?P<project_id>\d+)$', views.rate, name='rate'),
    url(r'^update_project/(?P<project_id>\d+)$', views.update_project,
        name='update_project'),
    url(r'^delete_project/(?P<project_id>\d+)$', views.delete_project,
        name='delete_project'),
    url(r'^export_rankings/(?P<project_id>\d+)$', views.export_rankings,
        name='export_rankings'),
    url(r'^export_ratings/(?P<project_id>\d+)$', views.export_ratings,
        name='export_ratings'),
)

