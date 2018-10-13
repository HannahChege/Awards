from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url('^$',views.award,name = 'award'),
    url(r'^profile/$', views.profile, name='profile'),
    # url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(?P<project_id>\d+)', views.add_comment, name='comment'), 
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)