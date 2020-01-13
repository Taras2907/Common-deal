from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import ugettext_lazy as _
from rest_framework.generics import get_object_or_404
from rest_auth.views import PasswordResetView
from django.contrib.sites.models import Site



