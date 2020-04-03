from django.urls import path
from . import views


urlpatterns = [
    path(
        'api/v1/applications/create',
        views.create_application,
        name='create_application'
    ),
    path(
        'api/v1/applications/',
        views.get_all_applications,
        name='get_all_applications'
    ),
    path(
        'api/test/',
        views.get_application_by_api_key,
        name='get_application_by_api_key'
    ),
    path(
        'api/v1/application/change_api_key',
        views.change_api_key,
        name='change_api_key'
    )
]
