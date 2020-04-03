from django.urls import path
from . import views


urlpatterns = [
    path(
        'api/v1/applications/',
        views.get_all_applications,
        name='get_all_applications'
    ),
    path(
        'api/test/<str:api_key>',
        views.get_application_by_api_key,
        name='get_application_by_api_key'
    )
]
