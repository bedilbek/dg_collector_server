from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from collector.models import Data
from collector.serializers import DataCreateSerializer


class DataViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Data.objects.all()
    serializer_class = DataCreateSerializer
    permission_classes = (AllowAny, )

    @action(methods=['GET'], detail=True, url_name='delete_data')
    def delete_data(self, request, pk):
        obj = self.get_object()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def data(request):
    d = Data.objects.all()
    l = []
    for index, datum in enumerate(d):
        l.append((index, {'t': datum.temperature, 'h': datum.humidity, 'g': datum.gas}))
    context = {
        'data': l
    }
    return render(request, template_name='data.html', context=context)
