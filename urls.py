from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from bug_tracker import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.ActiveBugs.as_view(), login_url='/bugs/login'), name='active_bugs'),
    url(r'^new/$', login_required(views.BugCreate.as_view(), login_url='/bugs/login'), name='bug_new'),
    url(r'^(?P<pk>\d+)', login_required(views.BugDetailView.as_view(), login_url='/bugs/login'), name='bug_detail'),
    url(r'^active/$', login_required(views.ActiveBugs.as_view(), login_url='/bugs/login'), name='active_bugs'),
    url(r'^all/$', login_required(views.BugList.as_view(), login_url='/bugs/login'), name='all_bugs'),
    url(r'^login/$', 'bug_tracker.views.login_user', name='login'),
    url(r'^logout/$', 'bug_tracker.views.logout_user', name='logout'),
    url(r'^assigned/(?P<pk>\d+)$', login_required(views.BugsAssigned.as_view(), login_url='bugs/login'), name='assigned'),
)
