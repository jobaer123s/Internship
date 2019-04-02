from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import create

urlpatterns = {
    # url(r'^postlists/$', CreateView.as_view(), name="create"),
    url(r'^postlists/$', create, name="create"),

}

urlpatterns = format_suffix_patterns(urlpatterns)