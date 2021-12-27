from django.contrib import admin

# Register your models here.

from myapp.models import Request_log


@admin.register(Request_log)
class Request_logAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "request_method", "request_path", "response_status", "request_body", 
    "remote_address", "server_hostname", "run_time", "timestamp"]
    