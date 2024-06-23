from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user = None
        if email:
            try:
                user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                pass
        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None
    

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None