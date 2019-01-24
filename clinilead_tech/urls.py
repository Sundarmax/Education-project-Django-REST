from django.contrib import admin
from django.urls import path
from qbuilder import views
from qbuilder.views import rules_ListAll,ques_ListAll,ques_List,topic_main,topic_mainList,login,create_User,subques_list,mainques_list
from qbuilder.views import rules_List
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^list/(?P<pk>[0-9]+)$',rules_List),
    path('list/',rules_ListAll),
    path('questions/',ques_ListAll),
    url(r'^questions/(?P<pk>[0-9]+)$',ques_List),
    path('maintopic',topic_main),
    url(r'^maintopic/(?P<pk>[0-9]+)$',topic_mainList),
    path('login/',login),
    path('user/',create_User),
    url(r'^subques/(?P<pk>[0-9]+)$',subques_list),
    url(r'^mainques/(?P<pk>[0-9]+)$',mainques_list),
    #url('mainques/',mainques_list)
]