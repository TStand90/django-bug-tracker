from django.contrib import admin

from bug_tracker.models import Bug

class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status')
    filter_horizontal = ('assigned_to',)

admin.site.register(Bug, BugAdmin)