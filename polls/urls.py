from django.conf.urls import url, include
from rest_framework import routers

from polls.views import QuestionViewSet
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)

app_name = 'polls'
urlpatterns = [
    # r'^$'  is a regular expression that matches an empty line.
    # ex: /polls/
    #url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^', include(router.urls)),
]

