from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^resumes/(?P<resume_id>\d+)/$', views.resume, name='your resume'),
    url(r'^search/', views.search, name='search'),
    url(r'^', views.start, name='start'),
]