from django.conf.urls import url
from snippets import views  # save as -->from .views import SnippetSerializer, Snippet


urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_detail)
]