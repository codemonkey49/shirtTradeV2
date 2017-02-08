from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r"profile",profile,name="profile"),
    url(r"browse",browse,name="browse"),
    url(r"detail/(?P<userName>.*)/",detail,name="detail"),
    url(r"messages/",messages,name="messages"),
    url(r"teamProfile/$",teamProfileView,name="teamProfile"),
    url(r"teamProfile/edit/(?P<shirtID>\d+)",editShirtView,name="editShirt"),

    ]