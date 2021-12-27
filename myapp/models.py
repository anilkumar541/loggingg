from django.db import models

# Create your models here.

class Request_log(models.Model):
    user_id=models.IntegerField(null=True)
    request_method=models.CharField(max_length=10)
    request_path=models.CharField(max_length=500)
    response_status=models.IntegerField()
    request_body=models.JSONField()
    remote_address=models.CharField(max_length=100)
    server_hostname=models.CharField(max_length=100)
    run_time=models.DecimalField(max_digits=10, decimal_places=10)
    timestamp=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'request_loggs'
        ordering = ['-timestamp']

        