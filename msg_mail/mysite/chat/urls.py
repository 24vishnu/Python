# from django.urls import path, re_path
#
# from .views import index, room
#
# app_name = 'chat'
# urlpatterns = [
#     path('', index, name='index'),
#     re_path(r'^(?P<room_name>[^/]+)/$', room, name='room')
# ]

from django.conf.urls import url, re_path
from django.urls import path
from .views import index, room, log_in, log_out, sign_up, user_list

app_name = 'chat'
urlpatterns = [
    path('start/', index, name='index'),
    path('chat/<room_name>/', room, name='room'),
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^log_out/$', log_out, name='log_out'),
    url(r'^sign_up/$', sign_up, name='sign_up'),
    url(r'^$', user_list, name='user_list')
]