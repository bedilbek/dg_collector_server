from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from collector.models import Data
from collector.serializers import DataCreateSerializer


class DataViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Data.objects.all()
    serializer_class = DataCreateSerializer
    permission_classes = (AllowAny, )
