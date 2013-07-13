from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r"^hal/$", views.message_classification, name="classifier"),
)
