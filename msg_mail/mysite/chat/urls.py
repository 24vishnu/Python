from django.conf.urls import url, re_path
from django.urls import path
from .views import create_Chat_Room, chat_room, log_in, log_out, sign_up, user_list, home, activate

app_name = 'chat'
urlpatterns = [
    path('start/', create_Chat_Room, name='index'),
    path('chat/<room_name>/', chat_room, name='room'),
    url(r'^login/$', log_in, name='log_in'),
    url(r'^logout/$', log_out, name='log_out'),
    url(r'^signup/$', sign_up, name='sign_up'),
    url(r'^list/$', user_list, name='user_list'),
    path('chat/activate/<token>/', activate, name='activate'),
    path('', home, name='home')
]