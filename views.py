from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import urllib

from bug_tracker.models import Bug


class BugCreate(CreateView):
    model = Bug
    success_url = '/bugs/active'

    def form_valid(self, form):
        title = form.cleaned_data['title']
        priority = form.cleaned_data['priority']
        status = form.cleaned_data['status']
        assigned_to = form.cleaned_data['assigned_to']
        comments = form.cleaned_data['comments']

        payload_string = ('Title: %s,'
                          'Priority: %s,'
                          'Status: %s,'
                          'Assigned To: %s,'
                          'Comments: %s'
                          % (title, priority, status, assigned_to, comments))

        payload_dict = '{ "channel": "#bottest", "username": "bugbot", "text": "%s" }' % payload_string

        data = urllib.parse.urlencode({'payload': payload_dict})

        data = data.encode('utf-8')
        request = urllib.request.Request("https://hooks.slack.com/services/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")
        request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")

        f = urllib.request.urlopen(request, data)

        return super(BugCreate, self).form_valid(form)


class BugDetailView(DetailView):
    model = Bug


class ActiveBugs(ListView):
    queryset = Bug.objects.filter(status='1')
    context_object_name = 'bugs_list'
    template_name = 'bug_tracker/bug_list_active.html'


class BugList(ListView):
    model = Bug
    context_object_name = 'bugs_list'


def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('active_bugs')
            else:
                error = 'Your account is disabled'
        else:
            error = 'Invalid username/password'

        return render(request, 'bug_tracker/login.html', {'errors': error})
    else:
        return render(request, 'bug_tracker/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


class BugsAssigned(ListView):
    model = Bug
    template_name = 'bug_tracker/bugs_assigned.html'
    context_object_name = 'bugs_list'

    def get_queryset(self):
        self.user = get_object_or_404(User, id=self.kwargs['pk'])
        return Bug.objects.filter(assigned_to=self.user)

    def get_context_data(self, **kwargs):
        context = super(BugsAssigned, self).get_context_data(**kwargs)
        context['assigned_user'] = self.user
        return context
