from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),

    path('login/', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^passwordReset/$', views.reset, name='resent'),
    path('signup/', views.signup, name='signup'),
    path('activate/<token>/', views.activate, name='activate'),
]
