from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView
)

from django.views.decorators.http import require_http_methods
from user.models import User
from .serializers import UserSerializer
from django.http import HttpResponse

# Use this class to sign up for a new user.
class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class DestroyUserView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilteringUserView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_name = self.request.query_params.get('user_name', None)
        pass_word = self.request.query_params.get('password', None)
        valid_users = User.objects.filter(user_name = user_name, password = pass_word)
        return valid_users