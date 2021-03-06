from rest_framework import serializers

from .models import MysqlStat, MysqlStatHis, MysqlSlowquery


class MysqlStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MysqlStat
        fields = '__all__'


class MysqlStatHisSerializer(serializers.ModelSerializer):
    class Meta:
        model = MysqlStatHis
        fields = '__all__'


class MysqlSlowquerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MysqlSlowquery
        fields = '__all__'
