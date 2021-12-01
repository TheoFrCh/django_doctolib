from django.http import HttpResponse
from django.contrib.auth import get_user_model


def index(request):
    user = get_user_model()
    users = user.objects.all()
    return HttpResponse(users)
