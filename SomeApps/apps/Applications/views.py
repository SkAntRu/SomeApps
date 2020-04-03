from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from Applications.models import Application
from Applications.serializers import ApplicationSerializer


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_application(request):
    """
    GET: return all applications

    POST: create new application.

        requirements:
            body={"title": 'Some Application', -- Required
                  "api_key": '7e58cde3e22d306ac49677d057000c41' -- Optional
            }
            api_key have to be string with 0 < len(api_key) <= 32
            If not implement "api_key", it will generate automatically"""
    if request.method == 'GET':
        try:
            apps = Application.objects.all()
        except Application.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ApplicationSerializer(apps, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = ApplicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def get_all_applications(request):
    """Return all applications"""
    all_apps = Application.objects.all()
    serializer = ApplicationSerializer(all_apps, many=True)
    if request.method == 'GET':
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_application_by_api_key(request):
    """GET: return all applications
    POST: return application with api_key=request.data['api_key']
        requirements:
            body={"api_key": "7e58cde3e22d306ac49677d057000c41"}"""
    if request.method == 'GET':
        try:
            apps = Application.objects.all()
        except Application.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ApplicationSerializer(apps, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            app = Application.objects.get(api_key=request.data['api_key'])
        except (Application.DoesNotExist, KeyError):
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ApplicationSerializer(app)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def change_api_key(request):
    """
    GET: return all applications

    POST: change api_key in application.
        Return True of Error Message

        requirements:
            body={"title": 'Some Application',
                  "new_api_key": '7e58cde3e22d306ac49677d057000c41'
            }
            api_key have to be string with 0 < len(api_key) <= 32"""
    if request.method == 'GET':
        try:
            apps = Application.objects.all()
        except Application.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ApplicationSerializer(apps, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            app = Application.objects.get(title=request.data['title'])
        except (Application.DoesNotExist, KeyError):
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            new_key = request.data['new_api_key']
        except KeyError:
            return Response({'error': 'indicate the api_key'})
        result = app.change_api_key(new_key)
        if result:
            return Response({'error': result})
        else:
            # return Response(status=status.HTTP_200_OK)
            serializer = ApplicationSerializer(app)
            return Response(serializer.data)
