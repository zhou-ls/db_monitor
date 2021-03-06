# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import DjangoModelPermissions

from utils.django_tools import NoPagination
from utils.tools import get_utctime, today, last_day
from .serializers import *


class ApiLinuxStat(ListCreateAPIView):
    serializer_class = LinuxStatSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        return LinuxStat.objects.filter(status=0, tags=tags).order_by('status')


class ApiLinuxStatHis(ListCreateAPIView):
    serializer_class = LinuxStatHisSerializer
    pagination_class = NoPagination
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)
        if start_time and end_time:
            start_time = get_utctime(start_time)
            end_time = get_utctime(end_time)
        else:
            # default data of 1 day
            end_time = today()
            start_time = last_day()
        return LinuxStatHis.objects.filter(tags=tags, check_time__gte=start_time, check_time__lte=end_time).order_by(
            'check_time')


# all instance
class ApiLinuxStatList(ListCreateAPIView):
    queryset = LinuxStat.objects.get_queryset().order_by('-status')
    serializer_class = LinuxStatSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('tags', 'host', 'status')
    search_fields = ('tags', 'host',)
    permission_classes = (DjangoModelPermissions,)


class ApiLinuxDisk(ListCreateAPIView):
    serializer_class = LinuxDiskSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        return LinuxDisk.objects.filter(tags=tags).order_by('-used_percent')


class ApiLinuxDiskHis(ListCreateAPIView):
    serializer_class = LinuxDiskSerializer
    pagination_class = NoPagination
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)
        if start_time and end_time:
            start_time = get_utctime(start_time)
            end_time = get_utctime(end_time)
        else:
            # default data of 1 day
            end_time = today()
            start_time = last_day()
        return LinuxDiskHis.objects.filter(tags=tags, check_time__gte=start_time, check_time__lte=end_time).order_by(
            'check_time')


class ApiLinuxIoStat(ListCreateAPIView):
    serializer_class = LinuxIoStatSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        return LinuxIoStat.objects.filter(tags=tags)


class ApiLinuxIoStatHis(ListCreateAPIView):
    serializer_class = LinuxIoStatSerializer
    pagination_class = NoPagination
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)
        if start_time and end_time:
            start_time = get_utctime(start_time)
            end_time = get_utctime(end_time)
        else:
            # default data of 1 day
            end_time = today()
            start_time = last_day()
        return LinuxIoStatHis.objects.filter(tags=tags, check_time__gte=start_time, check_time__lte=end_time).order_by(
            'check_time')
