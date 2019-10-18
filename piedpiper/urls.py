from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .users.views import UserViewSet, UserCreateViewSet
from django.views.generic import TemplateView
import django
from django.contrib.sitemaps.views import sitemap
from piedpiper.users.views import contact_mail
from allauth.account.views import confirm_email
#from django.views.generic.simple import redirect_to
from django.views.generic import RedirectView

#router = DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'users', UserCreateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts-rest/registration/account-confirm-email/(?P<key>.+)/', confirm_email, name='account_confirm_email'),
    path('api/v1/taskapp/', include('taskapp.urls')),
    path('api/v1/user/', include('piedpiper.users.urls')),
    path('api/v1/todo/',include('piedpiper.todo.urls')),
    path('email/', contact_mail),
    path('google33c69cf40535cfdb\.html/', lambda r: HttpResponse("google-site-verification: google33c69cf40535cfdb.html")),
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #path('/', TemplateView.as_view(template_name="base.html"), name='base'),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    #re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
    re_path(r'^$', TemplateView.as_view(template_name="index.html"), name='base'),
    #re_path(r'^$', RedirectView.as_view(url='https://vedantbari.pythonanywhere.com')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
