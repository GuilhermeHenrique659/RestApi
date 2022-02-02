from django.conf.urls import url
from .views import *

urlpatterns = [
	    url(r'^casa$', CasaList.as_view()),
]