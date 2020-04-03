from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Application
from .serializers import ApplicationSerializer


@api_view(['GET'])
def get_all_applications(request):
    """Return all applications"""
    all_apps = Application.objects.all()
    serializer = ApplicationSerializer(all_apps, many=True)
    if request.method == 'GET':
        return Response(serializer.data)


@api_view(['GET'])
def get_application_by_api_key(request, api_key):
    """Return application with api_key"""
    try:
        app = Application.objects.get(api_key=api_key)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ApplicationSerializer(app)
    if request.method == 'GET':
        return Response(serializer.data)
