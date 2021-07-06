from django.utils.timezone import now
from rest_framework.generics import (
    GenericAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from interviews.models import (
    Answer,
    Interview,
)
from interviews.serializers import (
    AnswerCreateSerializer,
    InterviewSerializer,
)


class InterviewViewSet(ListModelMixin,
                       GenericViewSet):
    serializer_class = InterviewSerializer

    def get_queryset(self):
        return Interview.objects.filter(start_date__lte=now(), end_date__gt=now())


class AnswerView(CreateModelMixin,
                 GenericAPIView):
    serializer_class = AnswerCreateSerializer

    def get_queryset(self):
        return Answer.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if (user := self.request.user).is_authenticated:
            serializer.save(user=user)
        else:
            serializer.save()
