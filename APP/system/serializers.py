from rest_framework.serializers import ModelSerializer
from .models import AlertLog, AlarmConf, AlarmInfo, SetupLog


class AlertLogSerializer(ModelSerializer):
    class Meta:
        model = AlertLog
        fields = '__all__'


class AlarmConfSerializer(ModelSerializer):
    class Meta:
        model = AlarmConf
        fields = '__all__'


class AlarmInfoSerializer(ModelSerializer):
    class Meta:
        model = AlarmInfo
        fields = '__all__'


class SetupLogSerializer(ModelSerializer):
    class Meta:
        model = SetupLog
        fields = '__all__'
