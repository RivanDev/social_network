from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.sign_in, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)