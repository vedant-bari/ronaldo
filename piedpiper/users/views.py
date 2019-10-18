from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib import messages
from django.http import HttpResponseRedirect

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def contact_mail(request):
       print(request.data)
       import requests

       request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(settings.ANYMAIL.get('MAILGUN_SENDER_DOMAIN'))
       try:
         send_mail = requests.post(request_url, auth=('api',  settings.ANYMAIL.get('MAILGUN_API_KEY')), data={
         'from' : request.data.get('email'),
         'to' : 'vedantbari40@gmail.com',
         'subject': request.data.get('subject'),
         'text' : request.data.get('user') + '  ' + request.data.get('message'),
        }
         )
         print(send_mail.text)
         messages.success(request, 'Your mail has been send successfully!')
         return HttpResponseRedirect('/')
         # return Response({"status":send_mail.text})
       except Exception as e:
         print(e)
         messages.error(request, 'Something went wrong while sending mail')
         return HttpResponseRedirect('/')
         # return Response({"status": "something went wrong"})
