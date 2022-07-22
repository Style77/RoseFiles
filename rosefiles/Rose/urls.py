from django.urls import path, re_path

from django.contrib import admin
from django.contrib.auth.views import LoginView

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login/', LoginView.as_view(template_name='admin/login.html')),
    path('upload/', views.model_form_upload),
    path('accounts/profile/', views.account_profile)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)