from django.urls import path

from . import views
#dynamic path segments should always be after static ones
urlpatterns = [
path('', views.index, name="all-meetups"), # our-domain.com/meetups
path('<slug:meetup_slug>/success', views.confirmation, name = 'email-confirmed-successfully'),
path('<slug:meetup_slug>', views.meetup_details, name="meetup-details"), # our-domain.com/meetups/<dynamic-path-segment>
]