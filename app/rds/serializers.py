from rest_framework import serializers

from app.rds.models import RedisStat, RedisStatHis


class RedisStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedisStat
        fields = '__all__'


class RedisStatHisSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedisStatHis
        fields = '__all__'


class RedisConfigSerializer(serializers.Serializer):
    config_name = serializers.CharField()
    config_value = serializers.CharField()
