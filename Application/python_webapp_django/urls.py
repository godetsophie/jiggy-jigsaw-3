"""
Definition of urls for python_webapp_django.
"""

from datetime import datetime
from django.urls import re_path
import django.contrib.auth.views
from django.views.static import serve
from django.conf import settings
import app.forms
import app.views as a_v
from app.views import signup_view

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    re_path(r'^$', app.views.home, name='home'),
    re_path(r'^contact$', app.views.contact, name='contact'),
    re_path(r'^about', app.views.about, name='about'),
    re_path(r'^play', app.views.about, name='play'),
    re_path(r'^login/$',
        django.contrib.auth.views.LoginView.as_view(),
        {
            'template_name': 'login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    re_path(r'^signup/', signup_view, name='signup'),
    re_path(r'^logout$',
        django.contrib.auth.views.LogoutView.as_view(),
        {
            'next_page': '/',
        },
        name='logout'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #re_path(r'^admin/', include(admin.site.urls)),
]
