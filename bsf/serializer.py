from rest_framework import serializers
from .models import Batch, Net, Laying


class BatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('id','farmId')


class NetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Net
        fields = ('id','farmId', 'netNumber')


class LayingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Laying
        fields = ('id','batchId', 'netId', 'layingStart', 'layingStartVideo',
                  'layingMidVideo', 'layingEnd', 'layingEndVideo', 'harvest',
                  'harveststatus', 'endResult', 'comment', 'leadId', 'approverId')

