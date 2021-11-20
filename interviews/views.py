from django.utils.timezone import now
from rest_framework.mixins import (
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from interviews.models import (
    Interview,
)
from interviews.serializers import (
    InterviewSerializer,
)


class InterviewViewSet(ListModelMixin,
                       GenericViewSet):

    def get_serializer_class(self):
        return InterviewSerializer

    def get_queryset(self):
        return Interview.objects.filter(start_date__lte=now(), end_date__gt=now())

    def perform_create(self, serializer):
        if (user := self.request.user).is_authenticated:
            serializer.update(instance=self.get_object(), validated_data={**serializer.validated_data, 'user': user})
        else:
            serializer.update(instance=self.get_object(), validated_data=serializer.validated_data)
