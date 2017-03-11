from django.conf.urls import url
from .views import index_view, create_view, url_redirection, url_view


urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^create$', create_view, name='create'),
    url(r'^([\w{}.-]{1,8})/$', url_redirection, name='url'),
    url(r'^v/([\w{}.-]{1,8})/$', url_view, name='view'),


]
