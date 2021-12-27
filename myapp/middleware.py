import socket
import time
import json
 
 
class RequestLogMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        self.start_time = time.time()
 
    def process_request(self, request):
        if request.method in ['POST', 'PUT', 'PATCH']:
            request.req_body = request.body
        return request
 
    def __call__(self, request):
        request = self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)
        return response
 
    def process_response(self, request, response):
        request_path = request.get_full_path()
        if not request_path.startswith('/api'):
            return response
        request_data = None
        content_type = request.META.get('CONTENT_TYPE',  'application/json')
        request_type = request.META.get('HTTP_ACCEPT', content_type)
        if request.method in ['POST', 'PUT', 'PATCH']:
            if content_type == 'application/json':
                request_data = json.loads(request.req_body)
        data = {
            "user_id": request.user.pk,
            "request_method": request.method,
            "request_path": request_path,
            "response_status": response.status_code,
            "remote_address": request.META['REMOTE_ADDR'],
            "server_hostname": socket.gethostname(),
            "request_body": request_data,
            "run_time": time.time() - self.start_time
        }
        return response
 
