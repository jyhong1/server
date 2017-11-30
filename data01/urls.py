from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^test_pd1_time',views.test_pd1_time),
    url(r'^test_pd1_time',views.test_pd2),

    url(r'^test',views.test),
    url(r'^index',views.index),
    url(r'^tutorial',views.index_tutorial),
    url(r'^about',views.about),

    url(r'^feedback',views.feedback_list),
    url(r'^feedback/(?P<pk>\d+)/$', views.feedback_detail, name='feedback_detail'),
    url(r'^feedback/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

]
