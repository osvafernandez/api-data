from .models import Projects
from rest_framework import viewsets, permissions
from .serializers import ProjectsSerialzers


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectsSerialzers
