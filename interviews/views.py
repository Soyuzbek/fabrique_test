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
    serializer_class = InterviewSerializer

    def get_queryset(self):
        return Interview.objects.filter(start_date__lte=now(), end_date__gt=now())
