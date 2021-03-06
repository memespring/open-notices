from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^about/?$', views.AboutView.as_view(), name='about'),
  url(r'^api/?$', views.APIView.as_view(), name='api'),
  url(r'^create-account/?$', views.RegistrationView.as_view(), name='register'),
  url(r'.well-known/acme-challenge/(?P<token>.+)', views.acme_challenge),
]