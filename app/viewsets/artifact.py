import json
import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from app.cloudinary_api.cloudinary_api import upload_file
from app.models import Artifact
from app.serializers import ArtifactSerializer


class ArtifactViewSet(viewsets.ModelViewSet):
    serializer_class = ArtifactSerializer
    queryset = Artifact.objects.all().order_by('-created_at')

    def get_queryset(self):
        filter = self.request.query_params.get('filter')
        filters = json.loads(filter)['filters']
        groom_id = filters.get('noivo_id', None)
        queryset = super().get_queryset()
        if groom_id is not None:
            queryset = queryset.filter(owner__id=groom_id)
        return queryset

    def create(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file was submitted'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            result = upload_file(file, str(uuid.uuid4()))
            request.data['public_id'] = result['public_id']
            request.data['link_url'] = result['secure_url']
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return super(ArtifactViewSet, self).create(request, *args, **kwargs)
