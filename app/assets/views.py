# encoding:utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import *


# Ecs Api   drf 中文文档   http://drf.jiuyou.info/#/drf/requests
class ApiOracleList(ListCreateAPIView):
    queryset = OracleList.objects.get_queryset().order_by('id')
    serializer_class = OracleListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('tags', 'host', 'db_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiOracleDetail(RetrieveUpdateDestroyAPIView):
    queryset = OracleList.objects.get_queryset().order_by('id')
    serializer_class = OracleListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMysqlList(ListCreateAPIView):
    queryset = MysqlList.objects.get_queryset().order_by('id')
    serializer_class = MysqlListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('tags', 'host', 'db_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiMysqlDetail(RetrieveUpdateDestroyAPIView):
    queryset = MysqlList.objects.get_queryset().order_by('id')
    serializer_class = MysqlListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiLinuxList(ListCreateAPIView):
    queryset = LinuxList.objects.get_queryset().order_by('id')
    serializer_class = LinuxListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('tags', 'host', 'linux_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiLinuxDetail(RetrieveUpdateDestroyAPIView):
    queryset = LinuxList.objects.get_queryset().order_by('id')
    serializer_class = LinuxListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiRedisList(ListCreateAPIView):
    queryset = RedisList.objects.get_queryset().order_by('id')
    serializer_class = RedisListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('tags', 'host', 'redis_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiRedisDetail(RetrieveUpdateDestroyAPIView):
    queryset = RedisList.objects.get_queryset().order_by('id')
    serializer_class = RedisListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
