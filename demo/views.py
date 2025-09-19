from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from .models import Weapon, Comment, Adv
from .permissions import IsOwnerOrReadOnly
from .serializers import WeaponSerializer, CommentSerializer, AdvSerializer


# Create your views here.

# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status': 'ОК'})

# class DemoView(APIView):
#     def get(self, request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status': 'ОК'})

class DemoView(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    def post(self, request):
        return Response({'status': 'ОК'})

class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user',]
    search_fields = ['text',]
    ordering_fields = ['id', 'user', 'text', 'created_at',]
    pagination_class = LimitOffsetPagination

class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)