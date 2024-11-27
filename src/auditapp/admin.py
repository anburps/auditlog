from django.contrib import admin
from auditlog.models import LogEntry
from auditlog.registry import auditlog

# Define a custom admin for LogEntry
class CustomLogEntryAdmin(admin.ModelAdmin):
    list_display = ('action', 'actor_email', 'timestamp')

    def actor_email(self, obj):
        # If the actor has an email attribute, return it, otherwise return "system"
        return obj.actor.email if obj.actor and hasattr(obj.actor, 'email') else "system"

    actor_email.short_description = 'Actor Email'

# Unregister the LogEntry model if it's already registered
try:
    admin.site.unregister(LogEntry)  # This will remove the default LogEntry registration by auditlog
except admin.sites.NotRegistered:
    pass  # LogEntry wasn't registered yet, so no issue

# Now, register LogEntry with the custom admin
admin.site.register(LogEntry, CustomLogEntryAdmin)
