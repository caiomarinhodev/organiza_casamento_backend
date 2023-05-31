from rest_framework import viewsets

from app.models import Idea
from app.serializers import IdeaSerializer


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
