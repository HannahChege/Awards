from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url('^$',views.award,name = 'award'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^newprofile/', views.new_profile, name='new_profile'),
    # url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url(r'^post/(?P<project_id>[0-9]+)/review_design/$', views.add_design, name='add_design'),
    url(r'^post/(?P<project_id>[0-9]+)/review_usability/$', views.add_usability, name='review_usability'),
    url(r'^post/(?P<project_id>[0-9]+)/review_content/$', views.add_content, name='review_content'),

]   
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)