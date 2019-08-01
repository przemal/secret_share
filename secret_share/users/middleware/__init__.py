class UserAgentTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            request.user.last_user_agent = request.META.get('HTTP_USER_AGENT', request.user.last_user_agent)
            request.user.save()
        return response
