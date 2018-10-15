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
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)