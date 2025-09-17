from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Weapon
from .serializers import WeaponSerializer
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