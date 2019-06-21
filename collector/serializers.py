from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from collector.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class DataCreateSerializer(serializers.Serializer):
    data = serializers.CharField()

    def validate(self, attrs):
        data: str = attrs.pop('data', '')
        values = list(map(float, data.split(';')))
        if len(values) < 3:
            raise ValidationError({'data': 'Error in data'})
        t = values[0]
        h = values[1]
        g = values[2]
        attrs['temperature'] = t
        attrs['humidity'] = h
        attrs['gas'] = g
        return attrs

    def create(self, validated_data):
        return Data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        raise NotImplemented('Update is not implemented')

    def to_representation(self, instance):
        return DataSerializer(instance).data
