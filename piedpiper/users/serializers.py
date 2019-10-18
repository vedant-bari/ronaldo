from rest_framework import serializers
from .models import User
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.utils import import_callable
from rest_framework import authentication
from rest_framework import exceptions

from django.contrib.auth import authenticate 
from django.conf import settings
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer, RegisterSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password1','password2')

        def get_cleaned_data(self):
            return {
                'first_name': self.validated_data.get('first_name', ''),
                'last_name': self.validated_data.get('last_name', ''),
                #'username': self.validated_data.get('username', ''),
                'password1': self.validated_data.get('password1', ''),
                'email': self.validated_data.get('email', ''),
                #'is_private' : self.validated_data.get('is_private', ''),
                #'is_adult' : self.validated_data.get('is_adult', '')
                }
        def save(self, request):
            adapter = get_adapter()
            user = adapter.new_user(request)
            self.cleaned_data = self.get_cleaned_data()
            print(self.cleaned_data)
            adapter.save_user(request, user, self)
            setup_user_email(request, user, [])

            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')

            user.save()
            return user  

class UserSerializer(serializers.ModelSerializer):
    #email = serializers.EmailField(required=False, allow_blank=True)
    #password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name',)
        #read_only_fields = ('username', )


class LoginSerializer(serializers.ModelSerializer):
    """Login Serialization for first_token"""
    email = serializers.EmailField(write_only=True)
    password  = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['email', 'password']
    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)    
    def authenticate(self, email, password):
        #username = request.META.get('HTTP_X_USERNAME')
        #if not username:
        #    return None

        try:
            user = User.objects.get(email=email,password = password)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)

    def _validate_phonenumber(self, email, password):
        user = None
        print("I am here")
        if email and password:
            
           user = authenticate(email=email, password=password)
            
           if not user:
               raise exceptions.AuthenticationFailed('No such user') 
           
        else:
            raise exceptions.ValidationError('phonenumber does not exist')
        return user

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = self._validate_phonenumber(email, password)
        attrs['user'] = user
        return attrs

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email', )


class JWTSerializer(serializers.Serializer):
    """
    Serializer for JWT authentication.
    """
    token = serializers.CharField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        """
        Required to allow using custom USER_DETAILS_SERIALIZER in
        JWTSerializer. Defining it here to avoid circular imports
        """
        rest_auth_serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})
        JWTUserDetailsSerializer = import_callable(
            rest_auth_serializers.get('USER_DETAILS_SERIALIZER', UserDetailsSerializer)
        )
        user_data = JWTUserDetailsSerializer(obj['user'], context=self.context).data
        return user_data



class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        print(validated_data['email'])
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id','password', 'first_name', 'last_name', 'email', 'auth_token',)
        read_only_fields = ('auth_token','username')
        extra_kwargs = {'password': {'write_only': True}}
