from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from .models import ApiKey


class ApiKeyManager(APIView):

    def post(self, request):
        key = get_random_string(length=40)
        description = request.data.get('description')
        api_key = ApiKey.objects.create(key=key, description=description)
        response = {'api_key': api_key.key}
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, key):
        try:
            api_key = ApiKey.objects.get(key=key, is_active=True)
        except ApiKey.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {'description': api_key.description,
                    'created': api_key.created}
        return Response(response, status=status.HTTP_200_OK)
