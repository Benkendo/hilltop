from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='homePage'),
    path('vehicle/<int:vehicle_id>/', views.vehicle_details, name='vehicle_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
