from .models import UserProfile

class EnsureUserProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                UserProfile.objects.get_or_create(user=request.user)
            except Exception as e:
                # Log the exception or handle it appropriately
                pass
        return self.get_response(request)