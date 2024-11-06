from rest_framework import serializers
from .models import Batch, Net, NetStat, Container, ContainerStat, Authority, StaffCurrent, StaffOrgChart

class AuthoritySerializers(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = ('id', 'tableName', 'farmId', 'view', 'add', 'edit',
                    'delete','accept', 'approve')

class StaffCurrentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffCurrent
        fields = ('id', 'staffId', 'position', 'level', 'pay',
                    'farmId','status', 'dataCreated', 'comments')

class StaffOrgChartSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffOrgChart
        fields = ('id', 'staffId', 'bossId', 'startDate', 'creatorSaffId', 'approvalSaffId',
                    'endDate','status')

class BatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('id','farmId')


class NetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Net
        fields = ('id','farmId', 'netNumber')


class NetStatSerializers(serializers.ModelSerializer):
    class Meta:
        model = NetStat
        fields = ('id', 'batchNumber' ,'netNumber', 'status', 'eggiesSetDate', 'eggiesRemovedDate', 'eggiesHarvested')

class ContainerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ('id', 'farmId' ,'containerName', 'containerType', 'containerUse')

class ContainerStatSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContainerStat
        fields = (
                    'id', 'batchNumber' ,'containerNumber',
                    'status', 'harveststage', 'setDate',
                    'removedDate', 'harvestWeight'
                )