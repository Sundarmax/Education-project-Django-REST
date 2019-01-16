from django.contrib import admin
from django.urls import path
from qbuilder import views
from qbuilder.views import rules_ListAll,rules_List,ques_ListAll,ques_List
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^list/(?P<pk>[0-9]+)$',rules_List),
    path('list/',rules_ListAll),
    path('questions/',ques_ListAll),
    url(r'^questions/(?P<pk>[0-9]+)$',ques_List)
]
