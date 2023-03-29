from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def generate_password_reset_link(email):
    user = User.objects.filter(email=email).first()
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    return uid + '/' + token + '/'


def _check_token_is_valid(pk_user, token):
    user = User.objects.filter(pk=pk_user).first()
    return default_token_generator.check_token(user, token)


def reset_link_is_valid(link):
    uid, token = link.split('/')
    pk = urlsafe_base64_decode(uid).decode()
    return _check_token_is_valid(pk, token)
